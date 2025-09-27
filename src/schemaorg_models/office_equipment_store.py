from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class OfficeEquipmentStore(Store):
    """
An office equipment store.
    """
    class_: Literal['https://schema.org/OfficeEquipmentStore'] = Field(default='https://schema.org/OfficeEquipmentStore', alias='@type', serialization_alias='@type') # type: ignore
