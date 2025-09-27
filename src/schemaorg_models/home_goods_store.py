from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class HomeGoodsStore(Store):
    """
A home goods store.
    """
    type_: Literal['https://schema.org/HomeGoodsStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HomeGoodsStore'),serialization_alias='class') # type: ignore
