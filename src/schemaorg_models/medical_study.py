from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity

from schemaorg_models.medical_entity import MedicalEntity
from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.administrative_area import AdministrativeArea

class MedicalStudy(MedicalEntity):
    """
A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.
    """
    studySubject: Optional[Union[MedicalEntity, List[MedicalEntity]]] = Field(default=None,validation_alias=AliasChoices('studySubject', 'https://schema.org/studySubject'),serialization_alias='https://schema.org/studySubject')
    sponsor: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),serialization_alias='https://schema.org/sponsor')
    status: Optional[Union["EventStatusType", List["EventStatusType"], "MedicalStudyStatus", List["MedicalStudyStatus"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('status', 'https://schema.org/status'),serialization_alias='https://schema.org/status')
    studyLocation: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(default=None,validation_alias=AliasChoices('studyLocation', 'https://schema.org/studyLocation'),serialization_alias='https://schema.org/studyLocation')
    healthCondition: Optional[Union["MedicalCondition", List["MedicalCondition"]]] = Field(default=None,validation_alias=AliasChoices('healthCondition', 'https://schema.org/healthCondition'),serialization_alias='https://schema.org/healthCondition')
