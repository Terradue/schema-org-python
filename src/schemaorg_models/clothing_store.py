from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ClothingStore(Store):
    """
A clothing store.
    """
    type_: Literal['https://schema.org/ClothingStore'] = Field(default='https://schema.org/ClothingStore', alias='@type', serialization_alias='@type') # type: ignore
