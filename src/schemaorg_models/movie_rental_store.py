from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MovieRentalStore(Store):
    """
A movie rental store.
    """
    class_: Literal['https://schema.org/MovieRentalStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
