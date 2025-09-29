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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_therapy import MedicalTherapy
    from .d_dx_element import DDxElement
    from .anatomical_structure import AnatomicalStructure
    from .event_status_type import EventStatusType
    from .drug import Drug
    from .superficial_anatomy import SuperficialAnatomy
    from .medical_sign_or_symptom import MedicalSignOrSymptom
    from .medical_test import MedicalTest
    from .medical_study_status import MedicalStudyStatus
    from .medical_risk_factor import MedicalRiskFactor
    from .anatomical_system import AnatomicalSystem
    from .medical_condition_stage import MedicalConditionStage

class MedicalCondition(MedicalEntity):
    '''
    Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.

    Attributes:
        associatedAnatomy: The anatomy of the underlying organ system or structures associated with this entity.
        signOrSymptom: A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition.
        possibleTreatment: A possible treatment to address this condition, sign or symptom.
        status: The status of the study (enumerated).
        typicalTest: A medical test typically performed given this condition.
        expectedPrognosis: The likely outcome in either the short term or long term of the medical condition.
        riskFactor: A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age,  coexisting condition.
        naturalProgression: The expected progression of the condition if it is not treated and allowed to progress naturally.
        secondaryPrevention: A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.
        drug: Specifying a drug or medicine used in a medication procedure.
        pathophysiology: Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.
        primaryPrevention: A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.
        differentialDiagnosis: One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.
        stage: The stage of the condition, if applicable.
        epidemiology: The characteristics of associated patients, such as age, gender, race etc.
        possibleComplication: A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.
    '''
    class_: Literal['https://schema.org/MedicalCondition'] = Field( # type: ignore
        default='https://schema.org/MedicalCondition',
        alias='@type',
        serialization_alias='@type'
    )
    associatedAnatomy: Optional[Union['AnatomicalSystem', List['AnatomicalSystem'], 'SuperficialAnatomy', List['SuperficialAnatomy'], 'AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    signOrSymptom: Optional[Union['MedicalSignOrSymptom', List['MedicalSignOrSymptom']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    possibleTreatment: Optional[Union['MedicalTherapy', List['MedicalTherapy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    status: Optional[Union['EventStatusType', List['EventStatusType'], 'MedicalStudyStatus', List['MedicalStudyStatus'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    typicalTest: Optional[Union['MedicalTest', List['MedicalTest']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expectedPrognosis: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    riskFactor: Optional[Union['MedicalRiskFactor', List['MedicalRiskFactor']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    naturalProgression: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    secondaryPrevention: Optional[Union['MedicalTherapy', List['MedicalTherapy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    drug: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    pathophysiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    primaryPrevention: Optional[Union['MedicalTherapy', List['MedicalTherapy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    differentialDiagnosis: Optional[Union['DDxElement', List['DDxElement']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    stage: Optional[Union['MedicalConditionStage', List['MedicalConditionStage']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    epidemiology: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    possibleComplication: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
