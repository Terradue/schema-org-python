from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class HardwareStore(Store):
    """
A hardware store.
    """
    class_: Literal['https://schema.org/HardwareStore'] = Field(default='https://schema.org/HardwareStore', alias='class', serialization_alias='class') # type: ignore
