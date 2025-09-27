from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class SportingGoodsStore(Store):
    """
A sporting goods store.
    """
    type_: Literal['https://schema.org/SportingGoodsStore'] = Field(default='https://schema.org/SportingGoodsStore', alias='@type', serialization_alias='@type') # type: ignore
