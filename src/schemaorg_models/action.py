from __future__ import annotations
from datetime import (
    datetime,
    time
)
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .virtual_location import VirtualLocation
    from .postal_address import PostalAddress
    from .entry_point import EntryPoint
    from .action_status_type import ActionStatusType
    from .how_to import HowTo
    from .person import Person
    from .organization import Organization
    from .place import Place

class Action(Thing):
    """
An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.\
\
See also [blog post](https://blog.schema.org/2014/04/16/announcing-schema-org-actions/) and [Actions overview document](https://schema.org/docs/actions.html).
    """
    class_: Literal['https://schema.org/Action'] = Field( # type: ignore
        default='https://schema.org/Action',
        alias='@type',
        serialization_alias='@type'
    )
    actionStatus: Optional[Union["ActionStatusType", List["ActionStatusType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionStatus',
            'https://schema.org/actionStatus'
        ),
        serialization_alias='https://schema.org/actionStatus'
    )
    target: Optional[Union[HttpUrl, List[HttpUrl], "EntryPoint", List["EntryPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'target',
            'https://schema.org/target'
        ),
        serialization_alias='https://schema.org/target'
    )
    instrument: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'instrument',
            'https://schema.org/instrument'
        ),
        serialization_alias='https://schema.org/instrument'
    )
    provider: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    actionProcess: Optional[Union["HowTo", List["HowTo"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionProcess',
            'https://schema.org/actionProcess'
        ),
        serialization_alias='https://schema.org/actionProcess'
    )
    agent: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'agent',
            'https://schema.org/agent'
        ),
        serialization_alias='https://schema.org/agent'
    )
    participant: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'participant',
            'https://schema.org/participant'
        ),
        serialization_alias='https://schema.org/participant'
    )
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endTime',
            'https://schema.org/endTime'
        ),
        serialization_alias='https://schema.org/endTime'
    )
    error: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'error',
            'https://schema.org/error'
        ),
        serialization_alias='https://schema.org/error'
    )
    result: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'result',
            'https://schema.org/result'
        ),
        serialization_alias='https://schema.org/result'
    )
    object: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'object',
            'https://schema.org/object'
        ),
        serialization_alias='https://schema.org/object'
    )
    location: Optional[Union["VirtualLocation", List["VirtualLocation"], "PostalAddress", List["PostalAddress"], str, List[str], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'location',
            'https://schema.org/location'
        ),
        serialization_alias='https://schema.org/location'
    )
    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startTime',
            'https://schema.org/startTime'
        ),
        serialization_alias='https://schema.org/startTime'
    )
