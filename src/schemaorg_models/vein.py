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
from .vessel import Vessel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .anatomical_system import AnatomicalSystem
    from .anatomical_structure import AnatomicalStructure

class Vein(Vessel):
    """
A type of blood vessel that specifically carries blood to the heart.
    """
    class_: Literal['https://schema.org/Vein'] = Field( # type: ignore
        default='https://schema.org/Vein',
        alias='@type',
        serialization_alias='@type'
    )
    regionDrained: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"], "AnatomicalSystem", List["AnatomicalSystem"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'regionDrained',
            'https://schema.org/regionDrained'
        ),
        serialization_alias='https://schema.org/regionDrained'
    )
    drainsTo: Optional[Union["Vessel", List["Vessel"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drainsTo',
            'https://schema.org/drainsTo'
        ),
        serialization_alias='https://schema.org/drainsTo'
    )
    tributary: Optional[Union["AnatomicalStructure", List["AnatomicalStructure"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tributary',
            'https://schema.org/tributary'
        ),
        serialization_alias='https://schema.org/tributary'
    )
