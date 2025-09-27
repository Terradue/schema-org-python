from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """
Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].
    """
    type_: Literal['https://schema.org/OccupationalExperienceRequirements'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OccupationalExperienceRequirements'),serialization_alias='class') # type: ignore
    monthsOfExperience: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('monthsOfExperience', 'https://schema.org/monthsOfExperience'),serialization_alias='https://schema.org/monthsOfExperience')
