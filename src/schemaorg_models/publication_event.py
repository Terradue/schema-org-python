from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class PublicationEvent(Event):
    """
A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type, e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.
    """
    type_: Literal['https://schema.org/PublicationEvent'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PublicationEvent'),serialization_alias='class') # type: ignore
    publishedBy: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('publishedBy', 'https://schema.org/publishedBy'),serialization_alias='https://schema.org/publishedBy')
    publishedOn: Optional[Union["BroadcastService", List["BroadcastService"]]] = Field(default=None,validation_alias=AliasChoices('publishedOn', 'https://schema.org/publishedOn'),serialization_alias='https://schema.org/publishedOn')
    free: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('free', 'https://schema.org/free'),serialization_alias='https://schema.org/free')
