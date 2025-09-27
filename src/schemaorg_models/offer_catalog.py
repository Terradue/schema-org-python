from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.item_list import ItemList


class OfferCatalog(ItemList):
    """
An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.
    """
    type_: Literal['https://schema.org/OfferCatalog'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OfferCatalog'),serialization_alias='class') # type: ignore
