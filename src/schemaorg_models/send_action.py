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
from .transfer_action import TransferAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .contact_point import ContactPoint
    from .audience import Audience
    from .delivery_method import DeliveryMethod
    from .person import Person
    from .organization import Organization

class SendAction(TransferAction):
    '''
    The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:\
\
* [[ReceiveAction]]: The reciprocal of SendAction.\
* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    Attributes:
        deliveryMethod: A sub property of instrument. The method of delivery.
        recipient: A sub property of participant. The participant who is at the receiving end of the action.
    '''
    class_: Literal['https://schema.org/SendAction'] = Field( # type: ignore
        default='https://schema.org/SendAction',
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
    recipient: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'ContactPoint', List['ContactPoint'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
