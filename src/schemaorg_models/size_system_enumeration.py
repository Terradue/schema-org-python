from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """
Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.
    """
    type_: Literal['https://schema.org/SizeSystemEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SizeSystemEnumeration'),serialization_alias='class') # type: ignore
