from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class OutletStore(Store):
    """
An outlet store.
    """
    class_: Literal['https://schema.org/OutletStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
