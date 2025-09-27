from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """
A shopping center or mall.
    """
    type_: Literal['https://schema.org/ShoppingCenter'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ShoppingCenter'),serialization_alias='class') # type: ignore
