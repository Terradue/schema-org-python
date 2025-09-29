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
    from .diet import Diet
    from .sports_team import SportsTeam
    from .sports_activity_location import SportsActivityLocation
    from .place import Place
    from .distance import Distance
    from .exercise_plan import ExercisePlan
    from .sports_event import SportsEvent
    from .person import Person

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
            'diet',
            'https://schema.org/diet'
        ),
        serialization_alias='https://schema.org/diet'
    )
    distance: Optional[Union['Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distance',
            'https://schema.org/distance'
        ),
        serialization_alias='https://schema.org/distance'
    )
    exerciseRelatedDiet: Optional[Union['Diet', List['Diet']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exerciseRelatedDiet',
            'https://schema.org/exerciseRelatedDiet'
        ),
        serialization_alias='https://schema.org/exerciseRelatedDiet'
    )
    exerciseCourse: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exerciseCourse',
            'https://schema.org/exerciseCourse'
        ),
        serialization_alias='https://schema.org/exerciseCourse'
    )
    exerciseType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exerciseType',
            'https://schema.org/exerciseType'
        ),
        serialization_alias='https://schema.org/exerciseType'
    )
    exercisePlan: Optional[Union['ExercisePlan', List['ExercisePlan']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exercisePlan',
            'https://schema.org/exercisePlan'
        ),
        serialization_alias='https://schema.org/exercisePlan'
    )
    course: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'course',
            'https://schema.org/course'
        ),
        serialization_alias='https://schema.org/course'
    )
    sportsEvent: Optional[Union['SportsEvent', List['SportsEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sportsEvent',
            'https://schema.org/sportsEvent'
        ),
        serialization_alias='https://schema.org/sportsEvent'
    )
    fromLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fromLocation',
            'https://schema.org/fromLocation'
        ),
        serialization_alias='https://schema.org/fromLocation'
    )
    sportsTeam: Optional[Union['SportsTeam', List['SportsTeam']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sportsTeam',
            'https://schema.org/sportsTeam'
        ),
        serialization_alias='https://schema.org/sportsTeam'
    )
    opponent: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'opponent',
            'https://schema.org/opponent'
        ),
        serialization_alias='https://schema.org/opponent'
    )
    sportsActivityLocation: Optional[Union['SportsActivityLocation', List['SportsActivityLocation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sportsActivityLocation',
            'https://schema.org/sportsActivityLocation'
        ),
        serialization_alias='https://schema.org/sportsActivityLocation'
    )
    toLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
