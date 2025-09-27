from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class TireShop(Store):
    """
A tire shop.
    """
    type_: Literal['https://schema.org/TireShop'] = Field(default='https://schema.org/TireShop', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
