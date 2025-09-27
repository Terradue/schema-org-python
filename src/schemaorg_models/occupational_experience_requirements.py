from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class OccupationalExperienceRequirements(Intangible):
    """
Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].
    """
    class_: Literal['https://schema.org/OccupationalExperienceRequirements'] = Field(default='https://schema.org/OccupationalExperienceRequirements', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    monthsOfExperience: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('monthsOfExperience', 'https://schema.org/monthsOfExperience'), serialization_alias='https://schema.org/monthsOfExperience')
