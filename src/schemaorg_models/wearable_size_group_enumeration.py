from typing import Literal
from pydantic import Field
from schemaorg_models.size_group_enumeration import SizeGroupEnumeration


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """
Enumerates common size groups (also known as "size types") for wearable products.
    """
    type_: Literal['https://schema.org/WearableSizeGroupEnumeration'] = Field(default='https://schema.org/WearableSizeGroupEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
