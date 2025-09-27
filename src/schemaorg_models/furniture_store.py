from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class FurnitureStore(Store):
    """
A furniture store.
    """
    class_: Literal['https://schema.org/FurnitureStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
