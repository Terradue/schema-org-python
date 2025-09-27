from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class BookStore(Store):
    """
A bookstore.
    """
    class_: Literal['https://schema.org/BookStore'] = Field(default='https://schema.org/BookStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
