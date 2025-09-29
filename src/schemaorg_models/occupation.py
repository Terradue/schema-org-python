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
    from .administrative_area import AdministrativeArea
    from .defined_term import DefinedTerm
    from .category_code import CategoryCode
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .monetary_amount import MonetaryAmount
    from .educational_occupational_credential import EducationalOccupationalCredential

class Occupation(Intangible):
    '''
    A profession, may involve prolonged training and/or a formal qualification.

    Attributes:
        occupationalCategory: A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.\

Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        occupationLocation:  The region/country for which this occupational description is appropriate. Note that educational requirements and qualifications can vary between jurisdictions.
        experienceRequirements: Description of skills and experience needed for the position or Occupation.
        responsibilities: Responsibilities associated with this role or Occupation.
        qualifications: Specific qualifications required for this role or Occupation.
        skills: A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is either claimed by a person, an organization or desired or required to fulfill a role or to work in an occupation.
        estimatedSalary: An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value.
        educationRequirements: Educational background needed for the position or Occupation.
    '''
    class_: Literal['https://schema.org/Occupation'] = Field( # type: ignore
        default='https://schema.org/Occupation',
        alias='@type',
        serialization_alias='@type'
    )
    occupationalCategory: Optional[Union['CategoryCode', List['CategoryCode'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
    occupationLocation: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationLocation',
            'https://schema.org/occupationLocation'
        ),
        serialization_alias='https://schema.org/occupationLocation'
    )
    experienceRequirements: Optional[Union['OccupationalExperienceRequirements', List['OccupationalExperienceRequirements'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'experienceRequirements',
            'https://schema.org/experienceRequirements'
        ),
        serialization_alias='https://schema.org/experienceRequirements'
    )
    responsibilities: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'responsibilities',
            'https://schema.org/responsibilities'
        ),
        serialization_alias='https://schema.org/responsibilities'
    )
    qualifications: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'qualifications',
            'https://schema.org/qualifications'
        ),
        serialization_alias='https://schema.org/qualifications'
    )
    skills: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'skills',
            'https://schema.org/skills'
        ),
        serialization_alias='https://schema.org/skills'
    )
    estimatedSalary: Optional[Union['MonetaryAmountDistribution', List['MonetaryAmountDistribution'], float, List[float], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedSalary',
            'https://schema.org/estimatedSalary'
        ),
        serialization_alias='https://schema.org/estimatedSalary'
    )
    educationRequirements: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationRequirements',
            'https://schema.org/educationRequirements'
        ),
        serialization_alias='https://schema.org/educationRequirements'
    )
