from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class FurnitureStore(Store):
    """
A furniture store.
    """
    type_: Literal['https://schema.org/FurnitureStore'] = Field(default='https://schema.org/FurnitureStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
