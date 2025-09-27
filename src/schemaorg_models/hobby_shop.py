from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class HobbyShop(Store):
    """
A store that sells materials useful or necessary for various hobbies.
    """
    class_: Literal['https://schema.org/HobbyShop'] = Field(default='https://schema.org/HobbyShop', alias='@type', serialization_alias='@type') # type: ignore
