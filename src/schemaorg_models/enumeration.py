from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .__class import _Class
from .property import Property
from .intangible import Intangible

class Enumeration(Intangible):
    """
Lists or enumerations—for example, a list of cuisines or music genres, etc.
    """
    class_: Literal['https://schema.org/Enumeration'] = Field( # type: ignore
        default='https://schema.org/Enumeration',
        alias='@type',
        serialization_alias='@type'
    )
    supersededBy: Optional[Union[Enumeration, List[Enumeration], _Class, List[_Class], Property, List[Property]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supersededBy',
            'https://schema.org/supersededBy'
        ),
        serialization_alias='https://schema.org/supersededBy'
    )
