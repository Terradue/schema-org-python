from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """
Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].
    """
    monthsOfExperience: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('monthsOfExperience', 'https://schema.org/monthsOfExperience'),serialization_alias='https://schema.org/monthsOfExperience')
