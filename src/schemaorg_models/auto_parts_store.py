from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class AutoPartsStore(Store):
    """
An auto parts store.
    """
    class_: Literal['https://schema.org/AutoPartsStore'] = Field(default='https://schema.org/AutoPartsStore', alias='class', serialization_alias='class') # type: ignore
