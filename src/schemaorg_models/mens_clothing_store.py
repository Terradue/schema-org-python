from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MensClothingStore(Store):
    """
A men's clothing store.
    """
    class_: Literal['https://schema.org/MensClothingStore'] = Field(default='https://schema.org/MensClothingStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
