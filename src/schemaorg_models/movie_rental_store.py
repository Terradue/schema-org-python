from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MovieRentalStore(Store):
    """
A movie rental store.
    """
    class_: Literal['https://schema.org/MovieRentalStore'] = Field(default='https://schema.org/MovieRentalStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
