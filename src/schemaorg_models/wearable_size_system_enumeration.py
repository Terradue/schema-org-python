from typing import Literal
from pydantic import Field
from schemaorg_models.size_system_enumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """
Enumerates common size systems specific for wearable products.
    """
    type_: Literal['https://schema.org/WearableSizeSystemEnumeration'] = Field(default='https://schema.org/WearableSizeSystemEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
