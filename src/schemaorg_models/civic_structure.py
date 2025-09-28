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
from .place import Place

class CivicStructure(Place):
    """
A public structure, such as a town hall or concert hall.
    """
    class_: Literal['https://schema.org/CivicStructure'] = Field( # type: ignore
        default='https://schema.org/CivicStructure',
        alias='@type',
        serialization_alias='@type'
    )
    openingHours: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'openingHours',
            'https://schema.org/openingHours'
        ),
        serialization_alias='https://schema.org/openingHours'
    )
