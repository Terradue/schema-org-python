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
from .trade_action import TradeAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .delivery_method import DeliveryMethod

class OrderAction(TradeAction):
    '''
    An agent orders an object/product/service to be delivered/sent.

    Attributes:
        deliveryMethod: A sub property of instrument. The method of delivery.
    '''
    class_: Literal['https://schema.org/OrderAction'] = Field( # type: ignore
        default='https://schema.org/OrderAction',
        alias='@type',
        serialization_alias='@type'
    )
    deliveryMethod: Optional[Union['DeliveryMethod', List['DeliveryMethod']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
