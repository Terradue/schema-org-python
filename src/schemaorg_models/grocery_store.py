from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class GroceryStore(Store):
    """
A grocery store.
    """
    type_: Literal['https://schema.org/GroceryStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GroceryStore'),serialization_alias='class') # type: ignore
