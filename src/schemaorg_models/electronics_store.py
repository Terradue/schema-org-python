from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ElectronicsStore(Store):
    """
An electronics store.
    """
    type_: Literal['https://schema.org/ElectronicsStore'] = Field(default='https://schema.org/ElectronicsStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
