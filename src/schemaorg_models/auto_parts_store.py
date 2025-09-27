from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class AutoPartsStore(Store):
    """
An auto parts store.
    """
    type_: Literal['https://schema.org/AutoPartsStore'] = Field(default='https://schema.org/AutoPartsStore', alias='@type', serialization_alias='@type') # type: ignore
