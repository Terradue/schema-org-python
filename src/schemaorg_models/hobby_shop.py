from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class HobbyShop(Store):
    """
A store that sells materials useful or necessary for various hobbies.
    """
    type_: Literal['https://schema.org/HobbyShop'] = Field(default='https://schema.org/HobbyShop', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
