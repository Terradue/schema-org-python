from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MensClothingStore(Store):
    """
A men's clothing store.
    """
    class_: Literal['https://schema.org/MensClothingStore'] = Field(default='https://schema.org/MensClothingStore', alias='@type', serialization_alias='@type') # type: ignore
