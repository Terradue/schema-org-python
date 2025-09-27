from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class HomeGoodsStore(Store):
    """
A home goods store.
    """
    class_: Literal['https://schema.org/HomeGoodsStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
