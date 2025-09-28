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
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem

class LymphaticVessel(Vessel):
    """
A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.
    """
    class_: Literal['https://schema.org/LymphaticVessel'] = Field( # type: ignore
        default='https://schema.org/LymphaticVessel',
        alias='@type',
        serialization_alias='@type'
    )
    regionDrained: Optional[Union[AnatomicalStructure, List[AnatomicalStructure], AnatomicalSystem, List[AnatomicalSystem]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'regionDrained',
            'https://schema.org/regionDrained'
        ),
        serialization_alias='https://schema.org/regionDrained'
    )
    runsTo: Optional[Union[Vessel, List[Vessel]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'runsTo',
            'https://schema.org/runsTo'
        ),
        serialization_alias='https://schema.org/runsTo'
    )
    originatesFrom: Optional[Union[Vessel, List[Vessel]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'originatesFrom',
            'https://schema.org/originatesFrom'
        ),
        serialization_alias='https://schema.org/originatesFrom'
    )
