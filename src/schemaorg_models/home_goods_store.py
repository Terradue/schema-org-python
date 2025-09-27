from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class HomeGoodsStore(Store):
    """
A home goods store.
    """
    type_: Literal['https://schema.org/HomeGoodsStore'] = Field(default='https://schema.org/HomeGoodsStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
