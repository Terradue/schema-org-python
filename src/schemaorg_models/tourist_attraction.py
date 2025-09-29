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
from .place import Place
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .audience import Audience
    from .language import Language

class TouristAttraction(Place):
    '''
    A tourist attraction.  In principle any Thing can be a [[TouristAttraction]], from a [[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]].  This Type can be used on its own to describe a general [[TouristAttraction]], or be used as an [[additionalType]] to add tourist attraction properties to any other type.  (See examples below)

    Attributes:
        touristType: Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular country, etc. 
        availableLanguage: A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
    '''
    class_: Literal['https://schema.org/TouristAttraction'] = Field( # type: ignore
        default='https://schema.org/TouristAttraction',
        alias='@type',
        serialization_alias='@type'
    )
    touristType: Optional[Union['Audience', List['Audience'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'touristType',
            'https://schema.org/touristType'
        ),
        serialization_alias='https://schema.org/touristType'
    )
    availableLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableLanguage',
            'https://schema.org/availableLanguage'
        ),
        serialization_alias='https://schema.org/availableLanguage'
    )
