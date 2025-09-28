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
from .person import Person
from .trade_action import TradeAction
from .organization import Organization
from .audience import Audience

class TipAction(TradeAction):
    """
The act of giving money voluntarily to a beneficiary in recognition of services rendered.
    """
    class_: Literal['https://schema.org/TipAction'] = Field( # type: ignore
        default='https://schema.org/TipAction',
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
