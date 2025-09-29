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
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .delivery_method import DeliveryMethod

class DeliveryEvent(Event):
    '''
    An event involving the delivery of an item.

    Attributes:
        availableThrough: After this date, the item will no longer be available for pickup.
        availableFrom: When the item is available for pickup from the store, locker, etc.
        hasDeliveryMethod: Method used for delivery or shipping.
        accessCode: Password, PIN, or access code needed for delivery (e.g. from a locker).
    '''
    class_: Literal['https://schema.org/DeliveryEvent'] = Field( # type: ignore
        default='https://schema.org/DeliveryEvent',
        alias='@type',
        serialization_alias='@type'
    )
    availableThrough: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    availableFrom: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasDeliveryMethod: Optional[Union['DeliveryMethod', List['DeliveryMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    accessCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
