from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class BikeStore(Store):
    """
A bike store.
    """
    class_: Literal['https://schema.org/BikeStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
