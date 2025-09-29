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
from .medical_intangible import MedicalIntangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .qualitative_value import QualitativeValue

class DoseSchedule(MedicalIntangible):
    '''
    A specific dosing schedule for a drug or supplement.

    Attributes:
        frequency: How often the dose is taken, e.g. 'daily'.
        doseValue: The value of the dose, e.g. 500.
        targetPopulation: Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.
        doseUnit: The unit of the dose, e.g. 'mg'.
    '''
    class_: Literal['https://schema.org/DoseSchedule'] = Field( # type: ignore
        default='https://schema.org/DoseSchedule',
        alias='@type',
        serialization_alias='@type'
    )
    frequency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'frequency',
            'https://schema.org/frequency'
        ),
        serialization_alias='https://schema.org/frequency'
    )
    doseValue: Optional[Union[float, List[float], 'QualitativeValue', List['QualitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doseValue',
            'https://schema.org/doseValue'
        ),
        serialization_alias='https://schema.org/doseValue'
    )
    targetPopulation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetPopulation',
            'https://schema.org/targetPopulation'
        ),
        serialization_alias='https://schema.org/targetPopulation'
    )
    doseUnit: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doseUnit',
            'https://schema.org/doseUnit'
        ),
        serialization_alias='https://schema.org/doseUnit'
    )
