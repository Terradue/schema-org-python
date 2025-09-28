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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .audience import Audience
    from .organization import Organization
    from .contact_point import ContactPoint
    from .person import Person

class ReturnAction(TransferAction):
    """
The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).
    """
    class_: Literal['https://schema.org/ReturnAction'] = Field( # type: ignore
        default='https://schema.org/ReturnAction',
        alias='@type',
        serialization_alias='@type'
    )
    recipient: Optional[Union["Organization", List["Organization"], "Audience", List["Audience"], "ContactPoint", List["ContactPoint"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
