from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class GardenStore(Store):
    """
A garden store.
    """
    class_: Literal['https://schema.org/GardenStore'] = Field(default='https://schema.org/GardenStore', alias='@type', serialization_alias='@type') # type: ignore
