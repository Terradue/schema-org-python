from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ElectronicsStore(Store):
    """
An electronics store.
    """
    class_: Literal['https://schema.org/ElectronicsStore'] = Field(default='https://schema.org/ElectronicsStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
