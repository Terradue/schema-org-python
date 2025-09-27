from typing import Literal
from pydantic import Field
from schemaorg_models.size_group_enumeration import SizeGroupEnumeration


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """
Enumerates common size groups (also known as "size types") for wearable products.
    """
    class_: Literal['https://schema.org/WearableSizeGroupEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
