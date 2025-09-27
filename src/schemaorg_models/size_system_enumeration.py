from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """
Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.
    """
    class_: Literal['https://schema.org/SizeSystemEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
