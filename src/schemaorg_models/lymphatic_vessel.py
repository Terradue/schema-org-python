from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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

class LymphaticVessel(Vessel):
    '''
    A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.

    Attributes:
        regionDrained: The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.
        runsTo: The vasculature the lymphatic structure runs, or efferents, to.
        originatesFrom: The vasculature the lymphatic structure originates, or afferents, from.
    '''
    class_: Literal['https://schema.org/LymphaticVessel'] = Field( # type: ignore
        default='https://schema.org/LymphaticVessel',
        alias='@type',
        serialization_alias='@type'
    )
    regionDrained: Optional[Union['AnatomicalStructure', List['AnatomicalStructure'], 'AnatomicalSystem', List['AnatomicalSystem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    runsTo: Optional[Union['Vessel', List['Vessel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    originatesFrom: Optional[Union['Vessel', List['Vessel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
