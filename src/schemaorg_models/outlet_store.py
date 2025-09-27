from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class OutletStore(Store):
    """
An outlet store.
    """
    class_: Literal['https://schema.org/OutletStore'] = Field(default='https://schema.org/OutletStore', alias='@type', serialization_alias='@type') # type: ignore
