from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ConvenienceStore(Store):
    """
A convenience store.
    """
    class_: Literal['https://schema.org/ConvenienceStore'] = Field(default='https://schema.org/ConvenienceStore', alias='class', serialization_alias='class') # type: ignore
