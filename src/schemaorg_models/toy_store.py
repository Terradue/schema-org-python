from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ToyStore(Store):
    """
A toy store.
    """
    class_: Literal['https://schema.org/ToyStore'] = Field(default='https://schema.org/ToyStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
