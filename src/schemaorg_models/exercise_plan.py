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
    from .duration import Duration
    from .energy import Energy
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
            'additionalVariable',
            'https://schema.org/additionalVariable'
        ),
        serialization_alias='https://schema.org/additionalVariable'
    )
    activityDuration: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activityDuration',
            'https://schema.org/activityDuration'
        ),
        serialization_alias='https://schema.org/activityDuration'
    )
    intensity: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'intensity',
            'https://schema.org/intensity'
        ),
        serialization_alias='https://schema.org/intensity'
    )
    repetitions: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'repetitions',
            'https://schema.org/repetitions'
        ),
        serialization_alias='https://schema.org/repetitions'
    )
    workload: Optional[Union['Energy', List['Energy'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workload',
            'https://schema.org/workload'
        ),
        serialization_alias='https://schema.org/workload'
    )
    restPeriods: Optional[Union['QuantitativeValue', List['QuantitativeValue'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'restPeriods',
            'https://schema.org/restPeriods'
        ),
        serialization_alias='https://schema.org/restPeriods'
    )
    activityFrequency: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'activityFrequency',
            'https://schema.org/activityFrequency'
        ),
        serialization_alias='https://schema.org/activityFrequency'
    )
    exerciseType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exerciseType',
            'https://schema.org/exerciseType'
        ),
        serialization_alias='https://schema.org/exerciseType'
    )
