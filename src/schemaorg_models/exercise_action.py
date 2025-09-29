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
from .play_action import PlayAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .sports_team import SportsTeam
    from .exercise_plan import ExercisePlan
    from .sports_activity_location import SportsActivityLocation
    from .sports_event import SportsEvent
    from .person import Person
    from .distance import Distance
    from .diet import Diet
    from .place import Place

class ExerciseAction(PlayAction):
    """
The act of participating in exertive activity for the purposes of improving health and fitness.
    """
    class_: Literal['https://schema.org/ExerciseAction'] = Field( # type: ignore
        default='https://schema.org/ExerciseAction',
        alias='@type',
        serialization_alias='@type'
    )
    diet: Optional[Union["Diet", List["Diet"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diet',
            'https://schema.org/diet'
        ),
        serialization_alias='https://schema.org/diet'
    )
    distance: Optional[Union["Distance", List["Distance"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distance',
            'https://schema.org/distance'
        ),
        serialization_alias='https://schema.org/distance'
    )
    exerciseRelatedDiet: Optional[Union["Diet", List["Diet"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exerciseRelatedDiet',
            'https://schema.org/exerciseRelatedDiet'
        ),
        serialization_alias='https://schema.org/exerciseRelatedDiet'
    )
    exerciseCourse: Optional[Union["Place", List["Place"]]] = Field(
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
    exercisePlan: Optional[Union["ExercisePlan", List["ExercisePlan"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exercisePlan',
            'https://schema.org/exercisePlan'
        ),
        serialization_alias='https://schema.org/exercisePlan'
    )
    course: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'course',
            'https://schema.org/course'
        ),
        serialization_alias='https://schema.org/course'
    )
    sportsEvent: Optional[Union["SportsEvent", List["SportsEvent"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sportsEvent',
            'https://schema.org/sportsEvent'
        ),
        serialization_alias='https://schema.org/sportsEvent'
    )
    fromLocation: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fromLocation',
            'https://schema.org/fromLocation'
        ),
        serialization_alias='https://schema.org/fromLocation'
    )
    sportsTeam: Optional[Union["SportsTeam", List["SportsTeam"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sportsTeam',
            'https://schema.org/sportsTeam'
        ),
        serialization_alias='https://schema.org/sportsTeam'
    )
    opponent: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'opponent',
            'https://schema.org/opponent'
        ),
        serialization_alias='https://schema.org/opponent'
    )
    sportsActivityLocation: Optional[Union["SportsActivityLocation", List["SportsActivityLocation"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sportsActivityLocation',
            'https://schema.org/sportsActivityLocation'
        ),
        serialization_alias='https://schema.org/sportsActivityLocation'
    )
    toLocation: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
