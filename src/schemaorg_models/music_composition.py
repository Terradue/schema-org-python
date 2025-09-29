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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .event import Event
    from .music_recording import MusicRecording
    from .organization import Organization
    from .person import Person

class MusicComposition(CreativeWork):
    '''
    A musical composition.

    Attributes:
        recordedAs: An audio recording of the work.
        composer: The person or organization who wrote a composition, or who is the composer of a work performed at some event.
        musicArrangement: An arrangement derived from the composition.
        lyrics: The words in the song.
        includedComposition: Smaller compositions included in this work (e.g. a movement in a symphony).
        musicalKey: The key, mode, or scale this composition uses.
        iswcCode: The International Standard Musical Work Code for the composition.
        lyricist: The person who wrote the words.
        musicCompositionForm: The type of composition (e.g. overture, sonata, symphony, etc.).
        firstPerformance: The date and place the work was first performed.
    '''
    class_: Literal['https://schema.org/MusicComposition'] = Field( # type: ignore
        default='https://schema.org/MusicComposition',
        alias='@type',
        serialization_alias='@type'
    )
    recordedAs: Optional[Union['MusicRecording', List['MusicRecording']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    composer: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    musicArrangement: Optional[Union['MusicComposition', List['MusicComposition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    lyrics: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    includedComposition: Optional[Union['MusicComposition', List['MusicComposition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    musicalKey: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    iswcCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    lyricist: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    musicCompositionForm: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    firstPerformance: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
