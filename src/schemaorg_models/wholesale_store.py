from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class WholesaleStore(Store):
    """
A wholesale store.
    """
    class_: Literal['https://schema.org/WholesaleStore'] = Field(default='https://schema.org/WholesaleStore', alias='@type', serialization_alias='@type') # type: ignore
