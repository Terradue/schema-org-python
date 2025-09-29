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
from .anatomical_structure import AnatomicalStructure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .nerve import Nerve
    from .vessel import Vessel

class Muscle(AnatomicalStructure):
    '''
    A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.

    Attributes:
        antagonist: The muscle whose action counteracts the specified muscle.
        insertion: The place of attachment of a muscle, or what the muscle moves.
        nerve: The underlying innervation associated with the muscle.
        bloodSupply: The blood vessel that carries blood from the heart to the muscle.
        muscleAction: The movement the muscle generates.
    '''
    class_: Literal['https://schema.org/Muscle'] = Field( # type: ignore
        default='https://schema.org/Muscle',
        alias='@type',
        serialization_alias='@type'
    )
    antagonist: Optional[Union['Muscle', List['Muscle']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    insertion: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    nerve: Optional[Union['Nerve', List['Nerve']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    bloodSupply: Optional[Union['Vessel', List['Vessel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    muscleAction: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
