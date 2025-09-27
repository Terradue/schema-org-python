from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """
A shopping center or mall.
    """
    class_: Literal['https://schema.org/ShoppingCenter'] = Field(default='https://schema.org/ShoppingCenter', alias='@type', serialization_alias='@type') # type: ignore
