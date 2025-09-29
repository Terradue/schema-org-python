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
    from .geo_shape import GeoShape
    from .thing import Thing
    from .place import Place
    from .media_subscription import MediaSubscription
    from .offer import Offer
    from .physical_activity_category import PhysicalActivityCategory
    from .category_code import CategoryCode

class ActionAccessSpecification(Intangible):
    '''
    A set of requirements that must be fulfilled in order to perform an Action.

    Attributes:
        requiresSubscription: Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').
        expectsAcceptanceOf: An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
        eligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.\
\
See also [[ineligibleRegion]].
    
        availabilityEnds: The end of the availability of the product or service included in the offer.
        ineligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\
\
See also [[eligibleRegion]].
      
        availabilityStarts: The beginning of the availability of the product or service included in the offer.
        category: A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
    '''
    class_: Literal['https://schema.org/ActionAccessSpecification'] = Field( # type: ignore
        default='https://schema.org/ActionAccessSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    requiresSubscription: Optional[Union[bool, List[bool], 'MediaSubscription', List['MediaSubscription']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expectsAcceptanceOf: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    eligibleRegion: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    availabilityEnds: Optional[Union[date, List[date], time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    ineligibleRegion: Optional[Union[str, List[str], 'Place', List['Place'], 'GeoShape', List['GeoShape']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    availabilityStarts: Optional[Union[datetime, List[datetime], date, List[date], time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    category: Optional[Union['PhysicalActivityCategory', List['PhysicalActivityCategory'], 'CategoryCode', List['CategoryCode'], str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
