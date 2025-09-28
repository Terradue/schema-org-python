from __future__ import annotations

from .medical_intangible import MedicalIntangible    

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
from schemaorg_models.qualitative_value import QualitativeValue

class DoseSchedule(MedicalIntangible):
    """
A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
    """
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
    doseValue: Optional[Union[float, List[float], QualitativeValue, List[QualitativeValue]]] = Field(
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
