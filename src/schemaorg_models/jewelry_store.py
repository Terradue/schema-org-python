from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class JewelryStore(Store):
    """
A jewelry store.
    """
    type_: Literal['https://schema.org/JewelryStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/JewelryStore'),serialization_alias='class') # type: ignore
