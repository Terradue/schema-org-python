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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .how_to import HowTo
    from .place import Place
    from .virtual_location import VirtualLocation
    from .action_status_type import ActionStatusType
    from .postal_address import PostalAddress
    from .person import Person
    from .organization import Organization
    from .entry_point import EntryPoint

class Action(Thing):
    '''
    An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.\
\
See also [blog post](https://blog.schema.org/2014/04/16/announcing-schema-org-actions/) and [Actions overview document](https://schema.org/docs/actions.html).

    Attributes:
        actionStatus: Indicates the current disposition of the Action.
        target: Indicates a target EntryPoint, or url, for an Action.
        instrument: The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        actionProcess: Description of the process by which the action was performed.
        agent: The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote a book.
        participant: Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*.
        endTime: The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.\
\
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        error: For failed actions, more information on the cause of the failure.
        result: The result produced in the action. E.g. John wrote *a book*.
        object: The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). E.g. John read *a book*.
        location: The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        startTime: The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.\
\
Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
    '''
    class_: Literal['https://schema.org/Action'] = Field( # type: ignore
        default='https://schema.org/Action',
        alias='@type',
        serialization_alias='@type'
    )
    actionStatus: Optional[Union['ActionStatusType', List['ActionStatusType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionStatus',
            'https://schema.org/actionStatus'
        ),
        serialization_alias='https://schema.org/actionStatus'
    )
    target: Optional[Union[HttpUrl, List[HttpUrl], 'EntryPoint', List['EntryPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'target',
            'https://schema.org/target'
        ),
        serialization_alias='https://schema.org/target'
    )
    instrument: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'instrument',
            'https://schema.org/instrument'
        ),
        serialization_alias='https://schema.org/instrument'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    actionProcess: Optional[Union['HowTo', List['HowTo']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionProcess',
            'https://schema.org/actionProcess'
        ),
        serialization_alias='https://schema.org/actionProcess'
    )
    agent: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'agent',
            'https://schema.org/agent'
        ),
        serialization_alias='https://schema.org/agent'
    )
    participant: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
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
    error: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'error',
            'https://schema.org/error'
        ),
        serialization_alias='https://schema.org/error'
    )
    result: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'result',
            'https://schema.org/result'
        ),
        serialization_alias='https://schema.org/result'
    )
    object: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'object',
            'https://schema.org/object'
        ),
        serialization_alias='https://schema.org/object'
    )
    location: Optional[Union['VirtualLocation', List['VirtualLocation'], 'PostalAddress', List['PostalAddress'], str, List[str], 'Place', List['Place']]] = Field(
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
