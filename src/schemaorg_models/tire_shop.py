from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class TireShop(Store):
    """
A tire shop.
    """
    type_: Literal['https://schema.org/TireShop'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TireShop'),serialization_alias='class') # type: ignore
