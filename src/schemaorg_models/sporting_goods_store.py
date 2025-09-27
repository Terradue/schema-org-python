from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class SportingGoodsStore(Store):
    """
A sporting goods store.
    """
    class_: Literal['https://schema.org/SportingGoodsStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
