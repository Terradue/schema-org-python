from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class BookStore(Store):
    """
A bookstore.
    """
    type_: Literal['https://schema.org/BookStore'] = Field(default='https://schema.org/BookStore', alias='@type', serialization_alias='@type') # type: ignore
