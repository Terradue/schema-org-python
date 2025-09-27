from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class MensClothingStore(Store):
    """
A men's clothing store.
    """
    type_: Literal['https://schema.org/MensClothingStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MensClothingStore'),serialization_alias='class') # type: ignore
