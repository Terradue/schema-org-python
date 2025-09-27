from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.size_group_enumeration import SizeGroupEnumeration


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """
Enumerates common size groups (also known as "size types") for wearable products.
    """
    type_: Literal['https://schema.org/WearableSizeGroupEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WearableSizeGroupEnumeration'),serialization_alias='class') # type: ignore
