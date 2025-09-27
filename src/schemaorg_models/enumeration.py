from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.property import Property

class Enumeration(Intangible):
    """
Lists or enumerations—for example, a list of cuisines or music genres, etc.
    """
    type_: Literal['https://schema.org/Enumeration'] = Field(default='https://schema.org/Enumeration', alias='@type', serialization_alias='@type') # type: ignore
    supersededBy: Optional[Union["Enumeration", List["Enumeration"], "_Class", List["_Class"], Property, List[Property]]] = Field(default=None, validation_alias=AliasChoices('supersededBy', 'https://schema.org/supersededBy'), serialization_alias='https://schema.org/supersededBy')
