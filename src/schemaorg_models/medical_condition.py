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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_therapy import MedicalTherapy
    from .drug import Drug
    from .medical_sign_or_symptom import MedicalSignOrSymptom
    from .medical_study_status import MedicalStudyStatus
    from .medical_test import MedicalTest
    from .d_dx_element import DDxElement
    from .medical_condition_stage import MedicalConditionStage
    from .anatomical_system import AnatomicalSystem
    from .medical_risk_factor import MedicalRiskFactor
    from .anatomical_structure import AnatomicalStructure
    from .event_status_type import EventStatusType
    from .superficial_anatomy import SuperficialAnatomy

class MedicalCondition(MedicalEntity):
    """
Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.
    """
    class_: Literal['https://schema.org/MedicalCondition'] = Field( # type: ignore
        default='https://schema.org/MedicalCondition',
        alias='@type',
        serialization_alias='@type'
    )
    associatedAnatomy: Optional[Union["AnatomicalSystem", List["AnatomicalSystem"], "SuperficialAnatomy", List["SuperficialAnatomy"], "AnatomicalStructure", List["AnatomicalStructure"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedAnatomy',
            'https://schema.org/associatedAnatomy'
        ),
        serialization_alias='https://schema.org/associatedAnatomy'
    )
    signOrSymptom: Optional[Union["MedicalSignOrSymptom", List["MedicalSignOrSymptom"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'signOrSymptom',
            'https://schema.org/signOrSymptom'
        ),
        serialization_alias='https://schema.org/signOrSymptom'
    )
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'possibleTreatment',
            'https://schema.org/possibleTreatment'
        ),
        serialization_alias='https://schema.org/possibleTreatment'
    )
    status: Optional[Union["EventStatusType", List["EventStatusType"], "MedicalStudyStatus", List["MedicalStudyStatus"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'status',
            'https://schema.org/status'
        ),
        serialization_alias='https://schema.org/status'
    )
    typicalTest: Optional[Union["MedicalTest", List["MedicalTest"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typicalTest',
            'https://schema.org/typicalTest'
        ),
        serialization_alias='https://schema.org/typicalTest'
    )
    expectedPrognosis: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectedPrognosis',
            'https://schema.org/expectedPrognosis'
        ),
        serialization_alias='https://schema.org/expectedPrognosis'
    )
    riskFactor: Optional[Union["MedicalRiskFactor", List["MedicalRiskFactor"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'riskFactor',
            'https://schema.org/riskFactor'
        ),
        serialization_alias='https://schema.org/riskFactor'
    )
    naturalProgression: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'naturalProgression',
            'https://schema.org/naturalProgression'
        ),
        serialization_alias='https://schema.org/naturalProgression'
    )
    secondaryPrevention: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'secondaryPrevention',
            'https://schema.org/secondaryPrevention'
        ),
        serialization_alias='https://schema.org/secondaryPrevention'
    )
    drug: Optional[Union["Drug", List["Drug"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drug',
            'https://schema.org/drug'
        ),
        serialization_alias='https://schema.org/drug'
    )
    pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pathophysiology',
            'https://schema.org/pathophysiology'
        ),
        serialization_alias='https://schema.org/pathophysiology'
    )
    primaryPrevention: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'primaryPrevention',
            'https://schema.org/primaryPrevention'
        ),
        serialization_alias='https://schema.org/primaryPrevention'
    )
    differentialDiagnosis: Optional[Union["DDxElement", List["DDxElement"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'differentialDiagnosis',
            'https://schema.org/differentialDiagnosis'
        ),
        serialization_alias='https://schema.org/differentialDiagnosis'
    )
    stage: Optional[Union["MedicalConditionStage", List["MedicalConditionStage"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'stage',
            'https://schema.org/stage'
        ),
        serialization_alias='https://schema.org/stage'
    )
    epidemiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'epidemiology',
            'https://schema.org/epidemiology'
        ),
        serialization_alias='https://schema.org/epidemiology'
    )
    possibleComplication: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'possibleComplication',
            'https://schema.org/possibleComplication'
        ),
        serialization_alias='https://schema.org/possibleComplication'
    )
