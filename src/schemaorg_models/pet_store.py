from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class PetStore(Store):
    """
A pet store.
    """
    type_: Literal['https://schema.org/PetStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PetStore'),serialization_alias='class') # type: ignore
