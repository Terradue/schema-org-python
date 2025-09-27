from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """
A list of possible conditions for the item.
    """
    type_: Literal['https://schema.org/OfferItemCondition'] = Field(default='https://schema.org/OfferItemCondition', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
