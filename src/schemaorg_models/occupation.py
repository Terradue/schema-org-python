from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
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
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .monetary_amount import MonetaryAmount
    from .administrative_area import AdministrativeArea
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .defined_term import DefinedTerm

class Occupation(Intangible):
    """
A profession, may involve prolonged training and/or a formal qualification.
    """
    class_: Literal['https://schema.org/Occupation'] = Field( # type: ignore
        default='https://schema.org/Occupation',
        alias='@type',
        serialization_alias='@type'
    )
    occupationalCategory: Optional[Union["CategoryCode", List["CategoryCode"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationalCategory',
            'https://schema.org/occupationalCategory'
        ),
        serialization_alias='https://schema.org/occupationalCategory'
    )
    occupationLocation: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'occupationLocation',
            'https://schema.org/occupationLocation'
        ),
        serialization_alias='https://schema.org/occupationLocation'
    )
    experienceRequirements: Optional[Union["OccupationalExperienceRequirements", List["OccupationalExperienceRequirements"], str, List[str]]] = Field(
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
    qualifications: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'qualifications',
            'https://schema.org/qualifications'
        ),
        serialization_alias='https://schema.org/qualifications'
    )
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'skills',
            'https://schema.org/skills'
        ),
        serialization_alias='https://schema.org/skills'
    )
    estimatedSalary: Optional[Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"], float, List[float], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'estimatedSalary',
            'https://schema.org/estimatedSalary'
        ),
        serialization_alias='https://schema.org/estimatedSalary'
    )
    educationRequirements: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationRequirements',
            'https://schema.org/educationRequirements'
        ),
        serialization_alias='https://schema.org/educationRequirements'
    )
