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
from .transfer_action import TransferAction
from .person import Person
from .organization import Organization
from .delivery_method import DeliveryMethod
from .audience import Audience

class ReceiveAction(TransferAction):
    """
The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.\
\
Related actions:\
\
* [[SendAction]]: The reciprocal of ReceiveAction.\
* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine).
    """
    class_: Literal['https://schema.org/ReceiveAction'] = Field( # type: ignore
        default='https://schema.org/ReceiveAction',
        alias='@type',
        serialization_alias='@type'
    )
    sender: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sender',
            'https://schema.org/sender'
        ),
        serialization_alias='https://schema.org/sender'
    )
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryMethod',
            'https://schema.org/deliveryMethod'
        ),
        serialization_alias='https://schema.org/deliveryMethod'
    )
