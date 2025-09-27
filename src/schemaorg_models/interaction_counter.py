from typing import List, Literal, Optional, Union
from datetime import datetime, time
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.action import Action
from schemaorg_models.virtual_location import VirtualLocation
from schemaorg_models.place import Place
from schemaorg_models.web_site import WebSite
from schemaorg_models.software_application import SoftwareApplication

class InteractionCounter(StructuredValue):
    """
A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.
    """
    class_: Literal['https://schema.org/InteractionCounter'] = Field(default='https://schema.org/InteractionCounter', alias='class', serialization_alias='class') # type: ignore
    interactionType: Optional[Union[Action, List[Action]]] = Field(default=None, validation_alias=AliasChoices('interactionType', 'https://schema.org/interactionType'), serialization_alias='https://schema.org/interactionType')
    userInteractionCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('userInteractionCount', 'https://schema.org/userInteractionCount'), serialization_alias='https://schema.org/userInteractionCount')
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('endTime', 'https://schema.org/endTime'), serialization_alias='https://schema.org/endTime')
    location: Optional[Union[VirtualLocation, List[VirtualLocation], "PostalAddress", List["PostalAddress"], str, List[str], Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('location', 'https://schema.org/location'), serialization_alias='https://schema.org/location')
    interactionService: Optional[Union[WebSite, List[WebSite], SoftwareApplication, List[SoftwareApplication]]] = Field(default=None, validation_alias=AliasChoices('interactionService', 'https://schema.org/interactionService'), serialization_alias='https://schema.org/interactionService')
    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('startTime', 'https://schema.org/startTime'), serialization_alias='https://schema.org/startTime')
