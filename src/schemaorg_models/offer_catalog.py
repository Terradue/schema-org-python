from __future__ import annotations

from .item_list import ItemList    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OfferCatalog(ItemList):
    """
An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.
    """
    class_: Literal['https://schema.org/OfferCatalog'] = Field( # type: ignore
        default='https://schema.org/OfferCatalog',
        alias='@type',
        serialization_alias='@type'
    )
