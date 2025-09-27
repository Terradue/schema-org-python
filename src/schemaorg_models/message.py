from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.person import Person
from schemaorg_models.creative_work import CreativeWork

class Message(CreativeWork):
    """
A single message from a sender to one or more organizations or people.
    """
    class_: Literal['https://schema.org/Message'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    dateReceived: Optional[Union[datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('dateReceived', 'https://schema.org/dateReceived'), serialization_alias='https://schema.org/dateReceived')
    dateRead: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('dateRead', 'https://schema.org/dateRead'), serialization_alias='https://schema.org/dateRead')
    dateSent: Optional[Union[datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('dateSent', 'https://schema.org/dateSent'), serialization_alias='https://schema.org/dateSent')
    sender: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('sender', 'https://schema.org/sender'), serialization_alias='https://schema.org/sender')
    bccRecipient: Optional[Union[Organization, List[Organization], "ContactPoint", List["ContactPoint"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('bccRecipient', 'https://schema.org/bccRecipient'), serialization_alias='https://schema.org/bccRecipient')
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], "ContactPoint", List["ContactPoint"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('recipient', 'https://schema.org/recipient'), serialization_alias='https://schema.org/recipient')
    messageAttachment: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('messageAttachment', 'https://schema.org/messageAttachment'), serialization_alias='https://schema.org/messageAttachment')
    ccRecipient: Optional[Union[Person, List[Person], "ContactPoint", List["ContactPoint"], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('ccRecipient', 'https://schema.org/ccRecipient'), serialization_alias='https://schema.org/ccRecipient')
    toRecipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person], "ContactPoint", List["ContactPoint"]]] = Field(default=None,validation_alias=AliasChoices('toRecipient', 'https://schema.org/toRecipient'), serialization_alias='https://schema.org/toRecipient')
