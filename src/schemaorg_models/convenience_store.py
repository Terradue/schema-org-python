from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ConvenienceStore(Store):
    """
A convenience store.
    """
    type_: Literal['https://schema.org/ConvenienceStore'] = Field(default='https://schema.org/ConvenienceStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
