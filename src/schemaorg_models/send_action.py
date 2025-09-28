from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .contact_point import ContactPoint
from .transfer_action import TransferAction
from .person import Person
from .organization import Organization
from .delivery_method import DeliveryMethod
from .audience import Audience

class SendAction(TransferAction):
    """
The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:\
\
* [[ReceiveAction]]: The reciprocal of SendAction.\
* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).
    """
    class_: Literal['https://schema.org/SendAction'] = Field( # type: ignore
        default='https://schema.org/SendAction',
        alias='@type',
        serialization_alias='@type'
    )
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryMethod',
            'https://schema.org/deliveryMethod'
        ),
        serialization_alias='https://schema.org/deliveryMethod'
    )
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
