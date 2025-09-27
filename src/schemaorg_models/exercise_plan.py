from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class ExercisePlan(CreativeWork):
    """
Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.
    """
    type_: Literal['https://schema.org/ExercisePlan'] = Field(default='https://schema.org/ExercisePlan', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    additionalVariable: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('additionalVariable', 'https://schema.org/additionalVariable'), serialization_alias='https://schema.org/additionalVariable')
    activityDuration: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Duration", List["Duration"]]] = Field(default=None, validation_alias=AliasChoices('activityDuration', 'https://schema.org/activityDuration'), serialization_alias='https://schema.org/activityDuration')
    intensity: Optional[Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('intensity', 'https://schema.org/intensity'), serialization_alias='https://schema.org/intensity')
    repetitions: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('repetitions', 'https://schema.org/repetitions'), serialization_alias='https://schema.org/repetitions')
    workload: Optional[Union["Energy", List["Energy"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('workload', 'https://schema.org/workload'), serialization_alias='https://schema.org/workload')
    restPeriods: Optional[Union["QuantitativeValue", List["QuantitativeValue"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('restPeriods', 'https://schema.org/restPeriods'), serialization_alias='https://schema.org/restPeriods')
    activityFrequency: Optional[Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('activityFrequency', 'https://schema.org/activityFrequency'), serialization_alias='https://schema.org/activityFrequency')
    exerciseType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('exerciseType', 'https://schema.org/exerciseType'), serialization_alias='https://schema.org/exerciseType')
