from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class JewelryStore(Store):
    """
A jewelry store.
    """
    class_: Literal['https://schema.org/JewelryStore'] = Field(default='https://schema.org/JewelryStore', alias='class', serialization_alias='class') # type: ignore
