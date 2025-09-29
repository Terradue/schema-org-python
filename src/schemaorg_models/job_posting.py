from __future__ import annotations
from datetime import (
    date,
    datetime
)
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .contact_point import ContactPoint
    from .price_specification import PriceSpecification
    from .organization import Organization
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .place import Place
    from .monetary_amount import MonetaryAmount
    from .occupation import Occupation
    from .administrative_area import AdministrativeArea
    from .person import Person
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .defined_term import DefinedTerm

class JobPosting(Intangible):
    """
A listing that describes a job opening in a certain organization.
    """
    class_: Literal['https://schema.org/JobPosting'] = Field( # type: ignore
        default='https://schema.org/JobPosting',
        alias='@type',
        serialization_alias='@type'
    )
    estimatedSalary: Optional[Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"], float, List[float], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedSalary',
            'https://schema.org/estimatedSalary'
        ),
        serialization_alias='https://schema.org/estimatedSalary'
    )
    directApply: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'directApply',
            'https://schema.org/directApply'
        ),
        serialization_alias='https://schema.org/directApply'
    )
    totalJobOpenings: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'totalJobOpenings',
            'https://schema.org/totalJobOpenings'
        ),
        serialization_alias='https://schema.org/totalJobOpenings'
    )
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'skills',
            'https://schema.org/skills'
        ),
        serialization_alias='https://schema.org/skills'
    )
    workHours: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workHours',
            'https://schema.org/workHours'
        ),
        serialization_alias='https://schema.org/workHours'
    )
    applicantLocationRequirements: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicantLocationRequirements',
            'https://schema.org/applicantLocationRequirements'
        ),
        serialization_alias='https://schema.org/applicantLocationRequirements'
    )
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough',
            'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough'
    )
    jobImmediateStart: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jobImmediateStart',
            'https://schema.org/jobImmediateStart'
        ),
        serialization_alias='https://schema.org/jobImmediateStart'
    )
    title: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'title',
            'https://schema.org/title'
        ),
        serialization_alias='https://schema.org/title'
    )
    employmentType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'employmentType',
            'https://schema.org/employmentType'
        ),
        serialization_alias='https://schema.org/employmentType'
    )
    salaryCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'salaryCurrency',
            'https://schema.org/salaryCurrency'
        ),
        serialization_alias='https://schema.org/salaryCurrency'
    )
    educationRequirements: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationRequirements',
            'https://schema.org/educationRequirements'
        ),
        serialization_alias='https://schema.org/educationRequirements'
    )
    benefits: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'benefits',
            'https://schema.org/benefits'
        ),
        serialization_alias='https://schema.org/benefits'
    )
    industry: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'industry',
            'https://schema.org/industry'
        ),
        serialization_alias='https://schema.org/industry'
    )
    sensoryRequirement: Optional[Union[HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sensoryRequirement',
            'https://schema.org/sensoryRequirement'
        ),
        serialization_alias='https://schema.org/sensoryRequirement'
    )
    incentives: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'incentives',
            'https://schema.org/incentives'
        ),
        serialization_alias='https://schema.org/incentives'
    )
    experienceInPlaceOfEducation: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'experienceInPlaceOfEducation',
            'https://schema.org/experienceInPlaceOfEducation'
        ),
        serialization_alias='https://schema.org/experienceInPlaceOfEducation'
    )
    applicationContact: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationContact',
            'https://schema.org/applicationContact'
        ),
        serialization_alias='https://schema.org/applicationContact'
    )
    occupationalCategory: Optional[Union["CategoryCode", List["CategoryCode"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
    physicalRequirement: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'physicalRequirement',
            'https://schema.org/physicalRequirement'
        ),
        serialization_alias='https://schema.org/physicalRequirement'
    )
    relevantOccupation: Optional[Union["Occupation", List["Occupation"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relevantOccupation',
            'https://schema.org/relevantOccupation'
        ),
        serialization_alias='https://schema.org/relevantOccupation'
    )
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePosted',
            'https://schema.org/datePosted'
        ),
        serialization_alias='https://schema.org/datePosted'
    )
    experienceRequirements: Optional[Union["OccupationalExperienceRequirements", List["OccupationalExperienceRequirements"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'experienceRequirements',
            'https://schema.org/experienceRequirements'
        ),
        serialization_alias='https://schema.org/experienceRequirements'
    )
    eligibilityToWorkRequirement: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibilityToWorkRequirement',
            'https://schema.org/eligibilityToWorkRequirement'
        ),
        serialization_alias='https://schema.org/eligibilityToWorkRequirement'
    )
    jobStartDate: Optional[Union[date, List[date], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jobStartDate',
            'https://schema.org/jobStartDate'
        ),
        serialization_alias='https://schema.org/jobStartDate'
    )
    specialCommitments: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'specialCommitments',
            'https://schema.org/specialCommitments'
        ),
        serialization_alias='https://schema.org/specialCommitments'
    )
    incentiveCompensation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'incentiveCompensation',
            'https://schema.org/incentiveCompensation'
        ),
        serialization_alias='https://schema.org/incentiveCompensation'
    )
    responsibilities: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'responsibilities',
            'https://schema.org/responsibilities'
        ),
        serialization_alias='https://schema.org/responsibilities'
    )
    employmentUnit: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'employmentUnit',
            'https://schema.org/employmentUnit'
        ),
        serialization_alias='https://schema.org/employmentUnit'
    )
    hiringOrganization: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hiringOrganization',
            'https://schema.org/hiringOrganization'
        ),
        serialization_alias='https://schema.org/hiringOrganization'
    )
    jobLocationType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jobLocationType',
            'https://schema.org/jobLocationType'
        ),
        serialization_alias='https://schema.org/jobLocationType'
    )
    jobLocation: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jobLocation',
            'https://schema.org/jobLocation'
        ),
        serialization_alias='https://schema.org/jobLocation'
    )
    employerOverview: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'employerOverview',
            'https://schema.org/employerOverview'
        ),
        serialization_alias='https://schema.org/employerOverview'
    )
    securityClearanceRequirement: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'securityClearanceRequirement',
            'https://schema.org/securityClearanceRequirement'
        ),
        serialization_alias='https://schema.org/securityClearanceRequirement'
    )
    baseSalary: Optional[Union[float, List[float], "PriceSpecification", List["PriceSpecification"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'baseSalary',
            'https://schema.org/baseSalary'
        ),
        serialization_alias='https://schema.org/baseSalary'
    )
    qualifications: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'qualifications',
            'https://schema.org/qualifications'
        ),
        serialization_alias='https://schema.org/qualifications'
    )
    jobBenefits: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jobBenefits',
            'https://schema.org/jobBenefits'
        ),
        serialization_alias='https://schema.org/jobBenefits'
    )
