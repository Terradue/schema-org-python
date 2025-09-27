from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class MovieRentalStore(Store):
    """
A movie rental store.
    """
    type_: Literal['https://schema.org/MovieRentalStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MovieRentalStore'),serialization_alias='class') # type: ignore
