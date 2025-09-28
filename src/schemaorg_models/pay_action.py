from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.trade_action import TradeAction

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
from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.contact_point import ContactPoint
from schemaorg_models.person import Person

class PayAction(TradeAction):
    """
An agent pays a price to a participant.
    """
    class_: Literal['https://schema.org/PayAction'] = Field( # type: ignore
        default='https://schema.org/PayAction',
        alias='@type',
        serialization_alias='@type'
    )
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
