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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .web_site import WebSite
    from .software_application import SoftwareApplication
    from .virtual_location import VirtualLocation
    from .action import Action
    from .place import Place
    from .postal_address import PostalAddress

class InteractionCounter(StructuredValue):
    '''
    A summary of how users have interacted with this CreativeWork. In most cases, authors will use a subtype to specify the specific type of interaction.

    Attributes:
        interactionType: The Action representing the type of interaction. For up votes, +1s, etc. use [[LikeAction]]. For down votes use [[DislikeAction]]. Otherwise, use the most specific Action.
        userInteractionCount: The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.
        endTime: The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.\
\
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        location: The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        interactionService: The WebSite or SoftwareApplication where the interactions took place.
        startTime: The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.\
\
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
    '''
    class_: Literal['https://schema.org/InteractionCounter'] = Field( # type: ignore
        default='https://schema.org/InteractionCounter',
        alias='@type',
        serialization_alias='@type'
    )
    interactionType: Optional[Union['Action', List['Action']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionType',
            'https://schema.org/interactionType'
        ),
        serialization_alias='https://schema.org/interactionType'
    )
    userInteractionCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'userInteractionCount',
            'https://schema.org/userInteractionCount'
        ),
        serialization_alias='https://schema.org/userInteractionCount'
    )
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endTime',
            'https://schema.org/endTime'
        ),
        serialization_alias='https://schema.org/endTime'
    )
    location: Optional[Union['VirtualLocation', List['VirtualLocation'], 'PostalAddress', List['PostalAddress'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'location',
            'https://schema.org/location'
        ),
        serialization_alias='https://schema.org/location'
    )
    interactionService: Optional[Union['WebSite', List['WebSite'], 'SoftwareApplication', List['SoftwareApplication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionService',
            'https://schema.org/interactionService'
        ),
        serialization_alias='https://schema.org/interactionService'
    )
    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startTime',
            'https://schema.org/startTime'
        ),
        serialization_alias='https://schema.org/startTime'
    )
