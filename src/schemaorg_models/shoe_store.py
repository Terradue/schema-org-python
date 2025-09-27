from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ShoeStore(Store):
    """
A shoe store.
    """
    type_: Literal['https://schema.org/ShoeStore'] = Field(default='https://schema.org/ShoeStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
