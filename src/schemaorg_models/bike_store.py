from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class BikeStore(Store):
    """
A bike store.
    """
    type_: Literal['https://schema.org/BikeStore'] = Field(default='https://schema.org/BikeStore', alias='@type', serialization_alias='@type') # type: ignore
