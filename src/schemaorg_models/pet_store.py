from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class PetStore(Store):
    """
A pet store.
    """
    class_: Literal['https://schema.org/PetStore'] = Field(default='https://schema.org/PetStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
