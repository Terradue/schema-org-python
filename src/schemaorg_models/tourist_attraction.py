from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class TouristAttraction(Place):
    """
A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)
    """
    type_: Literal['https://schema.org/TouristAttraction'] = Field(default='https://schema.org/TouristAttraction', alias='@type', serialization_alias='@type') # type: ignore
    touristType: Optional[Union["Audience", List["Audience"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('touristType', 'https://schema.org/touristType'), serialization_alias='https://schema.org/touristType')
    availableLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(default=None, validation_alias=AliasChoices('availableLanguage', 'https://schema.org/availableLanguage'), serialization_alias='https://schema.org/availableLanguage')
