from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class FurnitureStore(Store):
    """
A furniture store.
    """
    type_: Literal['https://schema.org/FurnitureStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FurnitureStore'),serialization_alias='class') # type: ignore
