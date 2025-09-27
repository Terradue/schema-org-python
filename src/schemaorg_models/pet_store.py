from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class PetStore(Store):
    """
A pet store.
    """
    class_: Literal['https://schema.org/PetStore'] = Field(default='https://schema.org/PetStore', alias='@type', serialization_alias='@type') # type: ignore
