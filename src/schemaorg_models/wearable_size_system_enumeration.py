from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.size_system_enumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """
Enumerates common size systems specific for wearable products.
    """
    type_: Literal['https://schema.org/WearableSizeSystemEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WearableSizeSystemEnumeration'),serialization_alias='class') # type: ignore
