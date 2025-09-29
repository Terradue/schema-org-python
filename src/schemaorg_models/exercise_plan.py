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
    from .energy import Energy
    from .duration import Duration
    from .quantitative_value import QuantitativeValue

class ExercisePlan(CreativeWork):
    '''
    Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.

    Attributes:
        additionalVariable: Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc.
        activityDuration: Length of time to engage in the activity.
        intensity: Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement.
        repetitions: Number of times one should repeat the activity.
        workload: Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure.
        restPeriods: How often one should break from the activity.
        activityFrequency: How often one should engage in the activity.
        exerciseType: Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.
    '''
    class_: Literal['https://schema.org/ExercisePlan'] = Field( # type: ignore
        default='https://schema.org/ExercisePlan',
        alias='@type',
        serialization_alias='@type'
    )
    additionalVariable: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    activityDuration: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    intensity: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    repetitions: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    workload: Optional[Union['Energy', List['Energy'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    restPeriods: Optional[Union['QuantitativeValue', List['QuantitativeValue'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    activityFrequency: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
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
