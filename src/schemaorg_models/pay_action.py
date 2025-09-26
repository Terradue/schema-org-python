from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.trade_action import TradeAction

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class PayAction(TradeAction):
    """
An agent pays a price to a participant.
    """
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'),serialization_alias='https://schema.org/recipient')
