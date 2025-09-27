from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ItemListOrderType(Enumeration):
    """
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
    type_: Literal['https://schema.org/ItemListOrderType'] = Field(default='https://schema.org/ItemListOrderType', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
