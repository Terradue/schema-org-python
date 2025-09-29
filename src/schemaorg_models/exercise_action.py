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
from .play_action import PlayAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .sports_event import SportsEvent
    from .sports_team import SportsTeam
    from .person import Person
    from .diet import Diet
    from .distance import Distance
    from .place import Place
    from .sports_activity_location import SportsActivityLocation
    from .exercise_plan import ExercisePlan

class ExerciseAction(PlayAction):
    '''
    The act of participating in exertive activity for the purposes of improving health and fitness.

    Attributes:
        diet: A sub property of instrument. The diet used in this action.
        distance: The distance travelled, e.g. exercising or travelling.
        exerciseRelatedDiet: A sub property of instrument. The diet used in this action.
        exerciseCourse: A sub property of location. The course where this action was taken.
        exerciseType: Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.
        exercisePlan: A sub property of instrument. The exercise plan used on this action.
        course: A sub property of location. The course where this action was taken.
        sportsEvent: A sub property of location. The sports event where this action occurred.
        fromLocation: A sub property of location. The original location of the object or the agent before the action.
        sportsTeam: A sub property of participant. The sports team that participated on this action.
        opponent: A sub property of participant. The opponent on this action.
        sportsActivityLocation: A sub property of location. The sports activity location where this action occurred.
        toLocation: A sub property of location. The final location of the object or the agent after the action.
    '''
    class_: Literal['https://schema.org/ExerciseAction'] = Field( # type: ignore
        default='https://schema.org/ExerciseAction',
        alias='@type',
        serialization_alias='@type'
    )
    diet: Optional[Union['Diet', List['Diet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    distance: Optional[Union['Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    exerciseRelatedDiet: Optional[Union['Diet', List['Diet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    exerciseCourse: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    exerciseType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    exercisePlan: Optional[Union['ExercisePlan', List['ExercisePlan']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    course: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sportsEvent: Optional[Union['SportsEvent', List['SportsEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    fromLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sportsTeam: Optional[Union['SportsTeam', List['SportsTeam']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    opponent: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sportsActivityLocation: Optional[Union['SportsActivityLocation', List['SportsActivityLocation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    toLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
