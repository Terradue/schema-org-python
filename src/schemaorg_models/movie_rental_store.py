from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MovieRentalStore(Store):
    """
A movie rental store.
    """
    type_: Literal['https://schema.org/MovieRentalStore'] = Field(default='https://schema.org/MovieRentalStore', alias='@type', serialization_alias='@type') # type: ignore
