from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.publication_event import PublicationEvent

from schemaorg_models.event import Event
from schemaorg_models.language import Language

class BroadcastEvent(PublicationEvent):
    """
An over the air or online broadcast event.
    """
    class_: Literal['https://schema.org/BroadcastEvent'] = Field(default='https://schema.org/BroadcastEvent', alias='@type', serialization_alias='@type') # type: ignore
    videoFormat: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('videoFormat', 'https://schema.org/videoFormat'), serialization_alias='https://schema.org/videoFormat')
    broadcastOfEvent: Optional[Union[Event, List[Event]]] = Field(default=None, validation_alias=AliasChoices('broadcastOfEvent', 'https://schema.org/broadcastOfEvent'), serialization_alias='https://schema.org/broadcastOfEvent')
    subtitleLanguage: Optional[Union[Language, List[Language], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('subtitleLanguage', 'https://schema.org/subtitleLanguage'), serialization_alias='https://schema.org/subtitleLanguage')
    isLiveBroadcast: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('isLiveBroadcast', 'https://schema.org/isLiveBroadcast'), serialization_alias='https://schema.org/isLiveBroadcast')
