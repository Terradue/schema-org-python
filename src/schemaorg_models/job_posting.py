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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .defined_term import DefinedTerm
    from .administrative_area import AdministrativeArea
    from .occupation import Occupation
    from .organization import Organization
    from .category_code import CategoryCode
    from .place import Place
    from .person import Person
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .contact_point import ContactPoint
    from .monetary_amount import MonetaryAmount
    from .price_specification import PriceSpecification
    from .educational_occupational_credential import EducationalOccupationalCredential

class JobPosting(Intangible):
    '''
    A listing that describes a job opening in a certain organization.

    Attributes:
        estimatedSalary: An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value.
        directApply: Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct application for the job, via the posting website. A job posting is considered to have directApply of [[True]] if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of [[False]] is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied.
        totalJobOpenings: The number of positions open for this job posting. Use a positive integer. Do not use if the number of positions is unclear or not known.
        skills: A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is either claimed by a person, an organization or desired or required to fulfill a role or to work in an occupation.
        workHours: The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).
        applicantLocationRequirements: The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This should not be used for citizenship or work visa requirements.
        validThrough: The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        jobImmediateStart: An indicator as to whether a position is available for an immediate start.
        title: The title of the job.
        employmentType: Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).
        salaryCurrency: The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee.
        educationRequirements: Educational background needed for the position or Occupation.
        benefits: Description of benefits associated with the job.
        industry: The industry associated with the job position.
        sensoryRequirement: A description of any sensory requirements and levels necessary to function on the job, including hearing and vision. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.
        incentives: Description of bonus and commission compensation aspects of the job.
        experienceInPlaceOfEducation: Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]]) in place of its formal educational qualifications (as indicated by [[educationRequirements]]). If true, indicates that satisfying one of these requirements is sufficient.
        applicationContact: Contact details for further information relevant to this job posting.
        occupationalCategory: A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\

Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        physicalRequirement: A description of the types of physical activity associated with the job. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.
        relevantOccupation: The Occupation for the JobPosting.
        datePosted: Publication date of an online listing.
        experienceRequirements: Description of skills and experience needed for the position or Occupation.
        eligibilityToWorkRequirement: The legal requirements such as citizenship, visa and other documentation required for an applicant to this job.
        jobStartDate: The date on which a successful applicant for this job would be expected to start work. Choose a specific date in the future or use the jobImmediateStart property to indicate the position is to be filled as soon as possible.
        specialCommitments: Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.
        incentiveCompensation: Description of bonus and commission compensation aspects of the job.
        responsibilities: Responsibilities associated with this role or Occupation.
        employmentUnit: Indicates the department, unit and/or facility where the employee reports and/or in which the job is to be performed.
        hiringOrganization: Organization or Person offering the job position.
        jobLocationType: A description of the job location (e.g. TELECOMMUTE for telecommute jobs).
        jobLocation: A (typically single) geographic location associated with the job position.
        employerOverview: A description of the employer, career opportunities and work environment for this position.
        securityClearanceRequirement: A description of any security clearance requirements of the job.
        baseSalary: The base salary of the job or of an employee in an EmployeeRole.
        qualifications: Specific qualifications required for this role or Occupation.
        jobBenefits: Description of benefits associated with the job.
    '''
    class_: Literal['https://schema.org/JobPosting'] = Field( # type: ignore
        default='https://schema.org/JobPosting',
        alias='@type',
        serialization_alias='@type'
    )
    estimatedSalary: Optional[Union['MonetaryAmountDistribution', List['MonetaryAmountDistribution'], float, List[float], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
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
    skills: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
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
    applicantLocationRequirements: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
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
    educationRequirements: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
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
    industry: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'industry',
            'https://schema.org/industry'
        ),
        serialization_alias='https://schema.org/industry'
    )
    sensoryRequirement: Optional[Union[HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
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
    applicationContact: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationContact',
            'https://schema.org/applicationContact'
        ),
        serialization_alias='https://schema.org/applicationContact'
    )
    occupationalCategory: Optional[Union['CategoryCode', List['CategoryCode'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
    physicalRequirement: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'physicalRequirement',
            'https://schema.org/physicalRequirement'
        ),
        serialization_alias='https://schema.org/physicalRequirement'
    )
    relevantOccupation: Optional[Union['Occupation', List['Occupation']]] = Field(
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
    experienceRequirements: Optional[Union['OccupationalExperienceRequirements', List['OccupationalExperienceRequirements'], str, List[str]]] = Field(
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
    employmentUnit: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'employmentUnit',
            'https://schema.org/employmentUnit'
        ),
        serialization_alias='https://schema.org/employmentUnit'
    )
    hiringOrganization: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
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
    jobLocation: Optional[Union['Place', List['Place']]] = Field(
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
    baseSalary: Optional[Union[float, List[float], 'PriceSpecification', List['PriceSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'baseSalary',
            'https://schema.org/baseSalary'
        ),
        serialization_alias='https://schema.org/baseSalary'
    )
    qualifications: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
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
