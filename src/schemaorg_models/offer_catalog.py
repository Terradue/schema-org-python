from typing import Literal
from pydantic import Field
from schemaorg_models.item_list import ItemList


class OfferCatalog(ItemList):
    """
An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.
    """
    class_: Literal['https://schema.org/OfferCatalog'] = Field(default='https://schema.org/OfferCatalog', alias='@type', serialization_alias='@type') # type: ignore
