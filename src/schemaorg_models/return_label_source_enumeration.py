from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """
Enumerates several types of return labels for product returns.
    """
    type_: Literal['https://schema.org/ReturnLabelSourceEnumeration'] = Field(default='https://schema.org/ReturnLabelSourceEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
