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
from .action import Action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .event import Event
    from .audience import Audience

class PlayAction(Action):
    '''
    The act of playing/exercising/training/performing for enjoyment, leisure, recreation, competition or exercise.\
\
Related actions:\
\
* [[ListenAction]]: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for an audience or at an event, rather than consuming music.\
* [[WatchAction]]: Unlike WatchAction (which is under ConsumeAction), PlayAction refers to showing/displaying for an audience or at an event, rather than consuming visual content.

    Attributes:
        audience: An intended audience, i.e. a group for whom something was created.
        event: Upcoming or past event associated with this place, organization, or action.
    '''
    class_: Literal['https://schema.org/PlayAction'] = Field( # type: ignore
        default='https://schema.org/PlayAction',
        alias='@type',
        serialization_alias='@type'
    )
    audience: Optional[Union['Audience', List['Audience']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audience',
            'https://schema.org/audience'
        ),
        serialization_alias='https://schema.org/audience'
    )
    event: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
