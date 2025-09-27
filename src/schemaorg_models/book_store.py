from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class BookStore(Store):
    """
A bookstore.
    """
    type_: Literal['https://schema.org/BookStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BookStore'),serialization_alias='class') # type: ignore
