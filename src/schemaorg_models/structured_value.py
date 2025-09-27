from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class StructuredValue(Intangible):
    """
Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    """
    type_: Literal['https://schema.org/StructuredValue'] = Field(default='https://schema.org/StructuredValue', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
