from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ToyStore(Store):
    """
A toy store.
    """
    class_: Literal['https://schema.org/ToyStore'] = Field(default='https://schema.org/ToyStore', alias='@type', serialization_alias='@type') # type: ignore
