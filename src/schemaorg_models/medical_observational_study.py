from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_study import MedicalStudy


class MedicalObservationalStudy(MedicalStudy):
    """
An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.
    """
    class_: Literal['https://schema.org/MedicalObservationalStudy'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    studyDesign: Optional[Union["MedicalObservationalStudyDesign", List["MedicalObservationalStudyDesign"]]] = Field(default=None,validation_alias=AliasChoices('studyDesign', 'https://schema.org/studyDesign'), serialization_alias='https://schema.org/studyDesign')
