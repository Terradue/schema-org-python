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
    from .contact_point import ContactPoint
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .monetary_amount import MonetaryAmount
    from .price_specification import PriceSpecification
    from .person import Person
    from .administrative_area import AdministrativeArea
    from .occupation import Occupation
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .place import Place
    from .defined_term import DefinedTerm
    from .organization import Organization
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .category_code import CategoryCode

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    directApply: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    totalJobOpenings: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    skills: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    workHours: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    applicantLocationRequirements: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    jobImmediateStart: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    title: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    employmentType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    salaryCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    educationRequirements: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    benefits: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    industry: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sensoryRequirement: Optional[Union[HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    incentives: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    experienceInPlaceOfEducation: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    applicationContact: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    occupationalCategory: Optional[Union['CategoryCode', List['CategoryCode'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    physicalRequirement: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    relevantOccupation: Optional[Union['Occupation', List['Occupation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    experienceRequirements: Optional[Union['OccupationalExperienceRequirements', List['OccupationalExperienceRequirements'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    eligibilityToWorkRequirement: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    jobStartDate: Optional[Union[date, List[date], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    specialCommitments: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    incentiveCompensation: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    responsibilities: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    employmentUnit: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hiringOrganization: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    jobLocationType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    jobLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    employerOverview: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    securityClearanceRequirement: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    baseSalary: Optional[Union[float, List[float], 'PriceSpecification', List['PriceSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    qualifications: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    jobBenefits: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
