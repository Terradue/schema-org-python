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
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization
    from .person import Person

class TipAction(TradeAction):
    '''
    The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    Attributes:
        recipient: A sub property of participant. The participant who is at the receiving end of the action.
    '''
    class_: Literal['https://schema.org/TipAction'] = Field( # type: ignore
        default='https://schema.org/TipAction',
        alias='@type',
        serialization_alias='@type'
    )
    recipient: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'ContactPoint', List['ContactPoint'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
