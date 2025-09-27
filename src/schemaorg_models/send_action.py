from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.transfer_action import TransferAction

from schemaorg_models.delivery_method import DeliveryMethod
from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class SendAction(TransferAction):
    """
The act of physically/electronically dispatching an object for transfer from an origin to a destination. Related actions:\
\
* [[ReceiveAction]]: The reciprocal of SendAction.\
* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I'm not necessarily giving it to you).
    """
    type_: Literal['https://schema.org/SendAction'] = Field(default='https://schema.org/SendAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    deliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(default=None, validation_alias=AliasChoices('deliveryMethod', 'https://schema.org/deliveryMethod'), serialization_alias='https://schema.org/deliveryMethod')
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'), serialization_alias='https://schema.org/recipient')
