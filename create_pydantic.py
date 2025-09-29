#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
import sys
from collections import defaultdict
from graphlib import TopologicalSorter
from keyword import kwlist
from pydantic import BaseModel
from typing import (
    Dict,
    MutableSequence,
    Optional,
    Set
)

from rdflib import RDF, RDFS, Graph, Namespace

SCHEMA = Namespace("https://schema.org/")
BASE_TYPES = {
    SCHEMA.Text: "str",
    SCHEMA.Number: "float",
    SCHEMA.Integer: "int",
    SCHEMA.Float: "float",
    SCHEMA.Boolean: "bool",
    SCHEMA.Date: "date",
    SCHEMA.DateTime: "datetime",
    SCHEMA.Time: "time",
    SCHEMA.URL: "HttpUrl",
    SCHEMA.XPathType: "str",
    SCHEMA.DataType: "str",
}
BASE_TYPES_STR = {str(k) for k in BASE_TYPES.keys()}

def parse_schema(content: str) -> Graph:
    g = Graph()
    g.parse(data=content, format="nt")
    return g


def to_protected_name(name: str) -> str:
    if name[0].isdigit() or name.lower() in kwlist:
        return f"_{name}"
    return name

def safe_name(name: str) -> str:
    clean_name = re.sub(r"[^a-zA-Z0-9]", "", name)
    return to_protected_name(clean_name[0].upper() + clean_name[1:])


def get_parent_class(graph: Graph, class_uri):
    for _, _, parent_uri in graph.triples((class_uri, RDFS.subClassOf, None)):
        if str(parent_uri).startswith(str(SCHEMA)):
            return safe_name(str(parent_uri).split("/")[-1])
    return None


def camel_to_snake(name):
    # Insert underscores before capital letters and lowercase the string
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscores before capital letters followed by lowercase letters
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    # Convert the entire string to lowercase
    return s2.lower()

class PropertyInfo(BaseModel):
    name: str
    types: MutableSequence[str] = []
    docstring: Optional[str] = None

class ClassInfo(BaseModel):
    imports: Set[str] = set([])
    name: str
    parent: Optional[str] = None
    docstring: Optional[str] = None
    order: int = 0
    properties: MutableSequence[PropertyInfo] = []

def set_docstring(graph: Graph, subject, info):
    for c_subject, c_predicate, c_object in graph.triples((subject, RDFS.comment, None)):
        info.docstring = (
            c_object.replace("\\n", "\n")
            .replace("\\(", "\\\\(")
            .replace("\\_", "\\\\_")
        )

def generate_models(graph: Graph):
    os.makedirs("src/schemaorg_models", exist_ok=True)

    classes: Dict[str, ClassInfo] = {}

    # First pass: collect class info
    for subject, predicate, object in graph.triples((None, RDF.type, RDFS.Class)):
        if str(subject).startswith(str(SCHEMA)) and str(subject) not in BASE_TYPES_STR:
            class_name = safe_name(str(subject).split("/")[-1])

            class_info: ClassInfo = ClassInfo(
                name=class_name,
                parent=get_parent_class(graph, subject)
            )

            classes[class_name] = class_info #{"parent": parent_class, "properties": []}

            # Extract comments into a docstring
            set_docstring(graph, subject, class_info)

            # Second pass: collect properties
            print(f"Collect properties for {subject}...")
            for s, p, o in graph.triples((None, SCHEMA.domainIncludes, subject)):
                prop_name = to_protected_name(str(s).split("/")[-1])

                property_info: PropertyInfo = PropertyInfo(
                    name=prop_name
                )

                print(f" * {prop_name}")
                set_docstring(graph, s, property_info)

                class_info.properties.append(property_info)

                for _, _, prop_range in graph.triples((s, SCHEMA.rangeIncludes, None)):
                    print(f"    - {prop_range}")
                    try:
                        if prop_range in BASE_TYPES:
                            python_type = BASE_TYPES[prop_range]
                            property_info.types.append(python_type)
                        else:
                            python_type = safe_name(str(prop_range).split("/")[-1])
                            
                            if python_type != class_info.parent and python_type != class_name:
                                class_info.imports.add(python_type)

                            property_info.types.append(f"'{python_type}'")
                    except Exception:
                        pass

    sorter = TopologicalSorter()
    ts_sorted = []

    for class_name, class_info in classes.items():
        sorter.add(class_name, class_info.parent)

    for order, class_name in enumerate(sorter.static_order()):
        if class_name is not None and class_name in classes:
            classes[class_name].order = order
            ts_sorted.append(class_name)

    # Write init file
    with open("src/schemaorg_models/__init__.py", "w") as f:
        f.write(f"__all__ = {str(ts_sorted)}\n\n")

        for class_name in ts_sorted:
            f.write(f"from .{camel_to_snake(class_name)} import {class_name}\n")

        for class_name in ts_sorted:
            class_info = classes.get(class_name)
            
            f.write(f"\ndef rebuild_{camel_to_snake(class_name)}():\n")

            for import_ in class_info.imports:
                f.write(f"    rebuild_{camel_to_snake(import_)}()\n")

            if class_info.parent:
                f.write(f"    rebuild_{camel_to_snake(class_info.parent)}()\n")
            
            f.write(f"    {class_name}.model_rebuild()\n")

    # Generate model files
    for class_name, class_info in classes.items():
        filename = f"src/schemaorg_models/{camel_to_snake(class_name)}.py"
        with open(filename, "w") as f:
            f.write("from __future__ import annotations\n")

            # Imports
            f.write("""from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
""")

            # Import parent class if exists
            if class_info.parent:
                f.write(f"from .{camel_to_snake(class_info.parent)} import {class_info.parent}\n")

            # add the type checking, if any import is required
            if class_info.imports:
                f.write("""from typing import TYPE_CHECKING
if TYPE_CHECKING:
""")
            for prop_type in class_info.imports:
                f.write(f"    from .{camel_to_snake(prop_type)} import {prop_type}\n")

            # Class definition
            if class_info.parent:
                f.write(f"\nclass {class_name}({class_info.parent}):\n")
            else:
                f.write(f"\nclass {class_name}(BaseModel):\n")

            f.write("    '''\n")
            f.write(f"    {class_info.docstring if class_info.docstring else 'Class description not available'}\n")

            if class_info.properties:
                f.write(f"\n    Attributes:\n")
                for property_info in class_info.properties:
                    f.write(f"        {property_info.name}: {property_info.docstring if property_info.docstring else 'Attribute description not available'}\n")

            f.write("    '''\n")

            if not class_info.parent:
                f.write("""    # global serializer for HttpUrl
    @field_serializer(HttpUrl, mode="plain")
    def serialize_httpurl(self, value: HttpUrl) -> str:
        return str(value)

""")

            # f.write("    model_config = ConfigDict(arbitrary_types_allowed=True)\n\n")

            # type class
            f.write(f"""    class_: Literal['https://schema.org/{class_name}'] = Field( # type: ignore
        default='https://schema.org/{class_name}',
        alias='@type',
        serialization_alias='@type'
    )
""")
            # Properties
            for property_info in class_info.properties:
                prop_types = ", ".join(
                    [f"{prop_type}, List[{prop_type}]" for prop_type in property_info.types]
                )

                variable_name = f"{property_info.name}_" if prop_name.lower() in kwlist else property_info.name
                	
                f.write(f"""    {variable_name}: Optional[Union[{prop_types}]] = Field(
        default=None,
        validation_alias=AliasChoices(
            '{prop_name}',
            'https://schema.org/{prop_name}'
        ),
        serialization_alias='https://schema.org/{prop_name}'
    )
""")
    return classes

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Generate pydantic models from schema.org"
    )

    # Add arguments
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    # Parse arguments
    args, rest = parser.parse_known_args()

    if len(rest) != 1:
        print("Need exactly one argument")

    content = open(rest[0]).read()

    print("Parsing RDF data...")
    graph = parse_schema(content)

    print("Generating Pydantic models...")
    generate_models(graph)

    print("Models generated in src/schemaorg_models directory")


if __name__ == "__main__":
    main()
