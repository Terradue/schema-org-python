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
from .property_value import PropertyValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .opening_hours_specification import OpeningHoursSpecification

class LocationFeatureSpecification(PropertyValue):
    '''
    Specifies a location feature by providing a structured value representing a feature of an accommodation as a property-value pair of varying degrees of formality.

    Attributes:
        validFrom: The date when the item becomes valid.
        hoursAvailable: The hours during which this service or contact is available.
        validThrough: The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
    '''
    class_: Literal['https://schema.org/LocationFeatureSpecification'] = Field( # type: ignore
        default='https://schema.org/LocationFeatureSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hoursAvailable: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
