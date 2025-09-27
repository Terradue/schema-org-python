from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class TireShop(Store):
    """
A tire shop.
    """
    class_: Literal['https://schema.org/TireShop'] = Field('class', alias='class', serialization_alias='class') # type: ignore
