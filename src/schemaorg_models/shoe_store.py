from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class ShoeStore(Store):
    """
A shoe store.
    """
    type_: Literal['https://schema.org/ShoeStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ShoeStore'),serialization_alias='class') # type: ignore
