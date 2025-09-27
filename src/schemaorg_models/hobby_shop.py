from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class HobbyShop(Store):
    """
A store that sells materials useful or necessary for various hobbies.
    """
    type_: Literal['https://schema.org/HobbyShop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HobbyShop'),serialization_alias='class') # type: ignore
