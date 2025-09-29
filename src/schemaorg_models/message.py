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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .audience import Audience
    from .contact_point import ContactPoint
    from .organization import Organization

class Message(CreativeWork):
    '''
    A single message from a sender to one or more organizations or people.

    Attributes:
        dateReceived: The date/time the message was received if a single recipient exists.
        dateRead: The date/time at which the message has been read by the recipient if a single recipient exists.
        dateSent: The date/time at which the message was sent.
        sender: A sub property of participant. The participant who is at the sending end of the action.
        bccRecipient: A sub property of recipient. The recipient blind copied on a message.
        recipient: A sub property of participant. The participant who is at the receiving end of the action.
        messageAttachment: A CreativeWork attached to the message.
        ccRecipient: A sub property of recipient. The recipient copied on a message.
        toRecipient: A sub property of recipient. The recipient who was directly sent the message.
    '''
    class_: Literal['https://schema.org/Message'] = Field( # type: ignore
        default='https://schema.org/Message',
        alias='@type',
        serialization_alias='@type'
    )
    dateReceived: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateReceived',
            'https://schema.org/dateReceived'
        ),
        serialization_alias='https://schema.org/dateReceived'
    )
    dateRead: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateRead',
            'https://schema.org/dateRead'
        ),
        serialization_alias='https://schema.org/dateRead'
    )
    dateSent: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateSent',
            'https://schema.org/dateSent'
        ),
        serialization_alias='https://schema.org/dateSent'
    )
    sender: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sender',
            'https://schema.org/sender'
        ),
        serialization_alias='https://schema.org/sender'
    )
    bccRecipient: Optional[Union['Organization', List['Organization'], 'ContactPoint', List['ContactPoint'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bccRecipient',
            'https://schema.org/bccRecipient'
        ),
        serialization_alias='https://schema.org/bccRecipient'
    )
    recipient: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'ContactPoint', List['ContactPoint'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
    messageAttachment: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'messageAttachment',
            'https://schema.org/messageAttachment'
        ),
        serialization_alias='https://schema.org/messageAttachment'
    )
    ccRecipient: Optional[Union['Person', List['Person'], 'ContactPoint', List['ContactPoint'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ccRecipient',
            'https://schema.org/ccRecipient'
        ),
        serialization_alias='https://schema.org/ccRecipient'
    )
    toRecipient: Optional[Union['Organization', List['Organization'], 'Audience', List['Audience'], 'Person', List['Person'], 'ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toRecipient',
            'https://schema.org/toRecipient'
        ),
        serialization_alias='https://schema.org/toRecipient'
    )
