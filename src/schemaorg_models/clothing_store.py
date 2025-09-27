from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class ClothingStore(Store):
    """
A clothing store.
    """
    type_: Literal['https://schema.org/ClothingStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ClothingStore'),serialization_alias='class') # type: ignore
