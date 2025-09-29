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
    from .person import Person
    from .contact_point import ContactPoint
    from .audience import Audience
    from .organization import Organization

class ReturnAction(TransferAction):
    '''
    The act of returning to the origin that which was previously received (concrete objects) or taken (ownership).

    Attributes:
        recipient: A sub property of participant. The participant who is at the receiving end of the action.
    '''
    class_: Literal['https://schema.org/ReturnAction'] = Field( # type: ignore
        default='https://schema.org/ReturnAction',
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
