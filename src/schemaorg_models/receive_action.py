from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.person import Person
from schemaorg_models.delivery_method import DeliveryMethod

class ReceiveAction(TransferAction):
    """
The act of physically/electronically taking delivery of an object that has been transferred from an origin to a destination. Reciprocal of SendAction.\
\
Related actions:\
\
* [[SendAction]]: The reciprocal of ReceiveAction.\
* [[TakeAction]]: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transferred (e.g. I can receive a package, but it does not mean the package is now mine).
    """
    class_: Literal['https://schema.org/ReceiveAction'] = Field(default='https://schema.org/ReceiveAction', alias='class', serialization_alias='class') # type: ignore
    sender: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('sender', 'https://schema.org/sender'), serialization_alias='https://schema.org/sender')
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None, validation_alias=AliasChoices('deliveryMethod', 'https://schema.org/deliveryMethod'), serialization_alias='https://schema.org/deliveryMethod')
