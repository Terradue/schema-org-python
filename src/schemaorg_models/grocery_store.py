from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class GroceryStore(Store):
    """
A grocery store.
    """
    class_: Literal['https://schema.org/GroceryStore'] = Field(default='https://schema.org/GroceryStore', alias='class', serialization_alias='class') # type: ignore
