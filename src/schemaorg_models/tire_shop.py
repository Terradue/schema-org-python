from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class TireShop(Store):
    """
A tire shop.
    """
    type_: Literal['https://schema.org/TireShop'] = Field(default='https://schema.org/TireShop', alias='@type', serialization_alias='@type') # type: ignore
