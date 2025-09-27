from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class WholesaleStore(Store):
    """
A wholesale store.
    """
    type_: Literal['https://schema.org/WholesaleStore'] = Field(default='https://schema.org/WholesaleStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
