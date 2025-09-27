from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.learning_resource import LearningResource

from schemaorg_models.language import Language
from schemaorg_models.structured_value import StructuredValue
from schemaorg_models.educational_occupational_credential import EducationalOccupationalCredential
from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.alignment_object import AlignmentObject
from schemaorg_models.course_instance import CourseInstance

class Course(LearningResource):
    """
A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.
    """
    type_: Literal['https://schema.org/Course'] = Field(default='https://schema.org/Course', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    availableLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(default=None, validation_alias=AliasChoices('availableLanguage', 'https://schema.org/availableLanguage'), serialization_alias='https://schema.org/availableLanguage')
    courseCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('courseCode', 'https://schema.org/courseCode'), serialization_alias='https://schema.org/courseCode')
    numberOfCredits: Optional[Union[int, List[int], StructuredValue, List[StructuredValue]]] = Field(default=None, validation_alias=AliasChoices('numberOfCredits', 'https://schema.org/numberOfCredits'), serialization_alias='https://schema.org/numberOfCredits')
    syllabusSections: Optional[Union["Syllabus", List["Syllabus"]]] = Field(default=None, validation_alias=AliasChoices('syllabusSections', 'https://schema.org/syllabusSections'), serialization_alias='https://schema.org/syllabusSections')
    educationalCredentialAwarded: Optional[Union[EducationalOccupationalCredential, List[EducationalOccupationalCredential], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('educationalCredentialAwarded', 'https://schema.org/educationalCredentialAwarded'), serialization_alias='https://schema.org/educationalCredentialAwarded')
    @field_serializer('educationalCredentialAwarded')
    def educationalCredentialAwarded2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    financialAidEligible: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('financialAidEligible', 'https://schema.org/financialAidEligible'), serialization_alias='https://schema.org/financialAidEligible')
    coursePrerequisites: Optional[Union["Course", List["Course"], AlignmentObject, List[AlignmentObject], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('coursePrerequisites', 'https://schema.org/coursePrerequisites'), serialization_alias='https://schema.org/coursePrerequisites')
    occupationalCredentialAwarded: Optional[Union[HttpUrl, List[HttpUrl], EducationalOccupationalCredential, List[EducationalOccupationalCredential], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('occupationalCredentialAwarded', 'https://schema.org/occupationalCredentialAwarded'), serialization_alias='https://schema.org/occupationalCredentialAwarded')
    @field_serializer('occupationalCredentialAwarded')
    def occupationalCredentialAwarded2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    totalHistoricalEnrollment: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('totalHistoricalEnrollment', 'https://schema.org/totalHistoricalEnrollment'), serialization_alias='https://schema.org/totalHistoricalEnrollment')
    hasCourseInstance: Optional[Union[CourseInstance, List[CourseInstance]]] = Field(default=None, validation_alias=AliasChoices('hasCourseInstance', 'https://schema.org/hasCourseInstance'), serialization_alias='https://schema.org/hasCourseInstance')
