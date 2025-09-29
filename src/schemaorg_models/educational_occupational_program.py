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
    from .offer import Offer
    from .defined_term import DefinedTerm
    from .day_of_week import DayOfWeek
    from .course import Course
    from .organization import Organization
    from .demand import Demand
    from .category_code import CategoryCode
    from .duration import Duration
    from .person import Person
    from .alignment_object import AlignmentObject
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .structured_value import StructuredValue
    from .educational_occupational_credential import EducationalOccupationalCredential

class EducationalOccupationalProgram(Intangible):
    '''
    A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    Attributes:
        timeToComplete: The expected length of time to complete the program if attending full-time.
        programType: The type of educational or occupational program. For example, classroom, internship, alternance, etc.
        applicationStartDate: The date at which the program begins collecting applications for the next enrollment cycle.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
        dayOfWeek: The day of the week for which these opening hours are valid.
        applicationDeadline: The date on which the program stops collecting applications for the next enrollment cycle. Flexible application deadlines (for example, a program with rolling admissions) can be described in a textual string, rather than as a DateTime.
        typicalCreditsPerTerm: The number of credits or units a full-time student would be expected to take in 1 term however 'term' is defined by the institution.
        educationalCredentialAwarded: A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.
        endDate: The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        salaryUponCompletion: The expected salary upon completing the training.
        numberOfCredits: The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.
        termsPerYear: The number of times terms of study are offered per year. Semesters and quarters are common units for term. For example, if the student can only take 2 semesters for the program in one year, then termsPerYear should be 2.
        educationalProgramMode: Similar to courseMode, the medium or means of delivery of the program as a whole. The value may either be a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous ).
        trainingSalary: The estimated salary earned while in the program.
        termDuration: The amount of time in a term as defined by the institution. A term is a length of time where students take one or more classes. Semesters and quarters are common units for term.
        timeOfDay: The time of day the program normally runs. For example, "evenings".
        maximumEnrollment: The maximum number of students who may be enrolled in the program.
        financialAidEligible: A financial aid type or program which students may use to pay for tuition or fees associated with the program.
        occupationalCredentialAwarded: A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.
        hasCourse: A course or class that is one of the learning opportunities that constitute an educational / occupational program. No information is implied about whether the course is mandatory or optional; no guarantee is implied about whether the course will be available to everyone on the program.
        occupationalCategory: A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\

Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        programPrerequisites: Prerequisites for enrolling in the program.
        startDate: The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    '''
    class_: Literal['https://schema.org/EducationalOccupationalProgram'] = Field( # type: ignore
        default='https://schema.org/EducationalOccupationalProgram',
        alias='@type',
        serialization_alias='@type'
    )
    timeToComplete: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'timeToComplete',
            'https://schema.org/timeToComplete'
        ),
        serialization_alias='https://schema.org/timeToComplete'
    )
    programType: Optional[Union[str, List[str], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programType',
            'https://schema.org/programType'
        ),
        serialization_alias='https://schema.org/programType'
    )
    applicationStartDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationStartDate',
            'https://schema.org/applicationStartDate'
        ),
        serialization_alias='https://schema.org/applicationStartDate'
    )
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    dayOfWeek: Optional[Union['DayOfWeek', List['DayOfWeek']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dayOfWeek',
            'https://schema.org/dayOfWeek'
        ),
        serialization_alias='https://schema.org/dayOfWeek'
    )
    applicationDeadline: Optional[Union[str, List[str], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicationDeadline',
            'https://schema.org/applicationDeadline'
        ),
        serialization_alias='https://schema.org/applicationDeadline'
    )
    typicalCreditsPerTerm: Optional[Union[int, List[int], 'StructuredValue', List['StructuredValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typicalCreditsPerTerm',
            'https://schema.org/typicalCreditsPerTerm'
        ),
        serialization_alias='https://schema.org/typicalCreditsPerTerm'
    )
    educationalCredentialAwarded: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalCredentialAwarded',
            'https://schema.org/educationalCredentialAwarded'
        ),
        serialization_alias='https://schema.org/educationalCredentialAwarded'
    )
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endDate',
            'https://schema.org/endDate'
        ),
        serialization_alias='https://schema.org/endDate'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    salaryUponCompletion: Optional[Union['MonetaryAmountDistribution', List['MonetaryAmountDistribution']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'salaryUponCompletion',
            'https://schema.org/salaryUponCompletion'
        ),
        serialization_alias='https://schema.org/salaryUponCompletion'
    )
    numberOfCredits: Optional[Union[int, List[int], 'StructuredValue', List['StructuredValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfCredits',
            'https://schema.org/numberOfCredits'
        ),
        serialization_alias='https://schema.org/numberOfCredits'
    )
    termsPerYear: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'termsPerYear',
            'https://schema.org/termsPerYear'
        ),
        serialization_alias='https://schema.org/termsPerYear'
    )
    educationalProgramMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalProgramMode',
            'https://schema.org/educationalProgramMode'
        ),
        serialization_alias='https://schema.org/educationalProgramMode'
    )
    trainingSalary: Optional[Union['MonetaryAmountDistribution', List['MonetaryAmountDistribution']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trainingSalary',
            'https://schema.org/trainingSalary'
        ),
        serialization_alias='https://schema.org/trainingSalary'
    )
    termDuration: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'termDuration',
            'https://schema.org/termDuration'
        ),
        serialization_alias='https://schema.org/termDuration'
    )
    timeOfDay: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'timeOfDay',
            'https://schema.org/timeOfDay'
        ),
        serialization_alias='https://schema.org/timeOfDay'
    )
    maximumEnrollment: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumEnrollment',
            'https://schema.org/maximumEnrollment'
        ),
        serialization_alias='https://schema.org/maximumEnrollment'
    )
    financialAidEligible: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'financialAidEligible',
            'https://schema.org/financialAidEligible'
        ),
        serialization_alias='https://schema.org/financialAidEligible'
    )
    occupationalCredentialAwarded: Optional[Union[HttpUrl, List[HttpUrl], 'EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCredentialAwarded',
            'https://schema.org/occupationalCredentialAwarded'
        ),
        serialization_alias='https://schema.org/occupationalCredentialAwarded'
    )
    hasCourse: Optional[Union['Course', List['Course']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCourse',
            'https://schema.org/hasCourse'
        ),
        serialization_alias='https://schema.org/hasCourse'
    )
    occupationalCategory: Optional[Union['CategoryCode', List['CategoryCode'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
    programPrerequisites: Optional[Union['AlignmentObject', List['AlignmentObject'], 'Course', List['Course'], 'EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programPrerequisites',
            'https://schema.org/programPrerequisites'
        ),
        serialization_alias='https://schema.org/programPrerequisites'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startDate',
            'https://schema.org/startDate'
        ),
        serialization_alias='https://schema.org/startDate'
    )
