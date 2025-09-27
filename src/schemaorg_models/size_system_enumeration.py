from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """
Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.
    """
    class_: Literal['https://schema.org/SizeSystemEnumeration'] = Field(default='https://schema.org/SizeSystemEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
