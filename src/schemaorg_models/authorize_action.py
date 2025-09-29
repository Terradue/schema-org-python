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
from .allocate_action import AllocateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .contact_point import ContactPoint
    from .audience import Audience
    from .organization import Organization
    from .person import Person

class AuthorizeAction(AllocateAction):
    '''
    The act of granting permission to an object.

    Attributes:
        recipient: A sub property of participant. The participant who is at the receiving end of the action.
    '''
    class_: Literal['https://schema.org/AuthorizeAction'] = Field( # type: ignore
        default='https://schema.org/AuthorizeAction',
        alias='@type',
        serialization_alias='@type'
    )
    recipient: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'ContactPoint', List['ContactPoint'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
