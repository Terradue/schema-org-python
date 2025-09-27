from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class FurnitureStore(Store):
    """
A furniture store.
    """
    class_: Literal['https://schema.org/FurnitureStore'] = Field(default='https://schema.org/FurnitureStore', alias='@type', serialization_alias='@type') # type: ignore
