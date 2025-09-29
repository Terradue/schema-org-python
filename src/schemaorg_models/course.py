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
from .learning_resource import LearningResource
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .course_instance import CourseInstance
    from .language import Language
    from .syllabus import Syllabus
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .structured_value import StructuredValue
    from .alignment_object import AlignmentObject
    from .defined_term import DefinedTerm

class Course(LearningResource):
    '''
    A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.

    Attributes:
        availableLanguage: A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        courseCode: The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001).
        numberOfCredits: The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.
        syllabusSections: Indicates (typically several) Syllabus entities that lay out what each section of the overall course will cover.
        educationalCredentialAwarded: A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.
        financialAidEligible: A financial aid type or program which students may use to pay for tuition or fees associated with the program.
        coursePrerequisites: Requirements for taking the Course. May be completion of another [[Course]] or a textual description like "permission of instructor". Requirements may be a pre-requisite competency, referenced using [[AlignmentObject]].
        occupationalCredentialAwarded: A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.
        totalHistoricalEnrollment: The total number of students that have enrolled in the history of the course.
        hasCourseInstance: An offering of the course at a specific time and place or through specific media or mode of study or to a specific section of students.
    '''
    class_: Literal['https://schema.org/Course'] = Field( # type: ignore
        default='https://schema.org/Course',
        alias='@type',
        serialization_alias='@type'
    )
    availableLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
    courseCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'courseCode',
            'https://schema.org/courseCode'
        ),
        serialization_alias='https://schema.org/courseCode'
    )
    numberOfCredits: Optional[Union[int, List[int], 'StructuredValue', List['StructuredValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfCredits',
            'https://schema.org/numberOfCredits'
        ),
        serialization_alias='https://schema.org/numberOfCredits'
    )
    syllabusSections: Optional[Union['Syllabus', List['Syllabus']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'syllabusSections',
            'https://schema.org/syllabusSections'
        ),
        serialization_alias='https://schema.org/syllabusSections'
    )
    educationalCredentialAwarded: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalCredentialAwarded',
            'https://schema.org/educationalCredentialAwarded'
        ),
        serialization_alias='https://schema.org/educationalCredentialAwarded'
    )
    financialAidEligible: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'financialAidEligible',
            'https://schema.org/financialAidEligible'
        ),
        serialization_alias='https://schema.org/financialAidEligible'
    )
    coursePrerequisites: Optional[Union['Course', List['Course'], 'AlignmentObject', List['AlignmentObject'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'coursePrerequisites',
            'https://schema.org/coursePrerequisites'
        ),
        serialization_alias='https://schema.org/coursePrerequisites'
    )
    occupationalCredentialAwarded: Optional[Union[HttpUrl, List[HttpUrl], 'EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCredentialAwarded',
            'https://schema.org/occupationalCredentialAwarded'
        ),
        serialization_alias='https://schema.org/occupationalCredentialAwarded'
    )
    totalHistoricalEnrollment: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalHistoricalEnrollment',
            'https://schema.org/totalHistoricalEnrollment'
        ),
        serialization_alias='https://schema.org/totalHistoricalEnrollment'
    )
    hasCourseInstance: Optional[Union['CourseInstance', List['CourseInstance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCourseInstance',
            'https://schema.org/hasCourseInstance'
        ),
        serialization_alias='https://schema.org/hasCourseInstance'
    )
