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
from .medical_study import MedicalStudy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_observational_study_design import MedicalObservationalStudyDesign

class MedicalObservationalStudy(MedicalStudy):
    '''
    An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.

    Attributes:
        studyDesign: Specifics about the observational study design (enumerated).
    '''
    class_: Literal['https://schema.org/MedicalObservationalStudy'] = Field( # type: ignore
        default='https://schema.org/MedicalObservationalStudy',
        alias='@type',
        serialization_alias='@type'
    )
    studyDesign: Optional[Union['MedicalObservationalStudyDesign', List['MedicalObservationalStudyDesign']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'studyDesign',
            'https://schema.org/studyDesign'
        ),
        serialization_alias='https://schema.org/studyDesign'
    )
