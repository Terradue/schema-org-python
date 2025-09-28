from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_study import MedicalStudy

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

class MedicalTrial(MedicalStudy):
    """
A medical trial is a type of medical study that uses a scientific process to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.
    """
    class_: Literal['https://schema.org/MedicalTrial'] = Field( # type: ignore
        default='https://schema.org/MedicalTrial',
        alias='@type',
        serialization_alias='@type'
    )
    trialDesign: Optional[Union["MedicalTrialDesign", List["MedicalTrialDesign"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trialDesign',
            'https://schema.org/trialDesign'
        ),
        serialization_alias='https://schema.org/trialDesign'
    )
