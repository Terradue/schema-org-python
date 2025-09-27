from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MensClothingStore(Store):
    """
A men's clothing store.
    """
    class_: Literal['https://schema.org/MensClothingStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
