from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ReturnMethodEnumeration(Enumeration):
    """
Enumerates several types of product return methods.
    """
    class_: Literal['https://schema.org/ReturnMethodEnumeration'] = Field(default='https://schema.org/ReturnMethodEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
