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
from .medical_study import MedicalStudy
from .medical_trial_design import MedicalTrialDesign

class MedicalTrial(MedicalStudy):
    """
A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.
    """
    class_: Literal['https://schema.org/MedicalTrial'] = Field( # type: ignore
        default='https://schema.org/MedicalTrial',
        alias='@type',
        serialization_alias='@type'
    )
    trialDesign: Optional[Union[MedicalTrialDesign, List[MedicalTrialDesign]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trialDesign',
            'https://schema.org/trialDesign'
        ),
        serialization_alias='https://schema.org/trialDesign'
    )
