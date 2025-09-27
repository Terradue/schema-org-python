from typing import Literal
from pydantic import Field
from schemaorg_models.size_system_enumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """
Enumerates common size systems specific for wearable products.
    """
    class_: Literal['https://schema.org/WearableSizeSystemEnumeration'] = Field(default='https://schema.org/WearableSizeSystemEnumeration', alias='@type', serialization_alias='@type') # type: ignore
