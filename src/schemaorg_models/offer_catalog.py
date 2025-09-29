from __future__ import annotations
from datetime import (
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
from .item_list import ItemList

class OfferCatalog(ItemList):
    '''
    An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.
    '''
    class_: Literal['https://schema.org/OfferCatalog'] = Field( # type: ignore
        default='https://schema.org/OfferCatalog',
        alias='@type',
        serialization_alias='@type'
    )
