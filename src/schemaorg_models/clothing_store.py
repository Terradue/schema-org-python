from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ClothingStore(Store):
    """
A clothing store.
    """
    class_: Literal['https://schema.org/ClothingStore'] = Field(default='https://schema.org/ClothingStore', alias='class', serialization_alias='class') # type: ignore
