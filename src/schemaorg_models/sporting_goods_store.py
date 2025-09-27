from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class SportingGoodsStore(Store):
    """
A sporting goods store.
    """
    type_: Literal['https://schema.org/SportingGoodsStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SportingGoodsStore'),serialization_alias='class') # type: ignore
