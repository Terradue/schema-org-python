from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.administrative_area import AdministrativeArea

class Occupation(Intangible):
    """
A profession, may involve prolonged training and/or a formal qualification.
    """
    type_: Literal['https://schema.org/Occupation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Occupation'),serialization_alias='class') # type: ignore
    occupationalCategory: Optional[Union["CategoryCode", List["CategoryCode"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('occupationalCategory', 'https://schema.org/occupationalCategory'),serialization_alias='https://schema.org/occupationalCategory')
    occupationLocation: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(default=None,validation_alias=AliasChoices('occupationLocation', 'https://schema.org/occupationLocation'),serialization_alias='https://schema.org/occupationLocation')
    experienceRequirements: Optional[Union["OccupationalExperienceRequirements", List["OccupationalExperienceRequirements"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('experienceRequirements', 'https://schema.org/experienceRequirements'),serialization_alias='https://schema.org/experienceRequirements')
    responsibilities: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('responsibilities', 'https://schema.org/responsibilities'),serialization_alias='https://schema.org/responsibilities')
    qualifications: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('qualifications', 'https://schema.org/qualifications'),serialization_alias='https://schema.org/qualifications')
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('skills', 'https://schema.org/skills'),serialization_alias='https://schema.org/skills')
    estimatedSalary: Optional[Union["MonetaryAmountDistribution", List["MonetaryAmountDistribution"], float, List[float], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None,validation_alias=AliasChoices('estimatedSalary', 'https://schema.org/estimatedSalary'),serialization_alias='https://schema.org/estimatedSalary')
    educationRequirements: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('educationRequirements', 'https://schema.org/educationRequirements'),serialization_alias='https://schema.org/educationRequirements')
