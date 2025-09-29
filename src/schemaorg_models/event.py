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
    from .review import Review
    from .schedule import Schedule
    from .event_status_type import EventStatusType
    from .audience import Audience
    from .place import Place
    from .quantitative_value import QuantitativeValue
    from .offer import Offer
    from .aggregate_rating import AggregateRating
    from .demand import Demand
    from .creative_work import CreativeWork
    from .duration import Duration
    from .postal_address import PostalAddress
    from .performing_group import PerformingGroup
    from .organization import Organization
    from .language import Language
    from .virtual_location import VirtualLocation
    from .person import Person
    from .defined_term import DefinedTerm
    from .event_attendance_mode_enumeration import EventAttendanceModeEnumeration
    from .grant import Grant

class Event(Thing):
    '''
    An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the [[offers]] property. Repeated events may be structured as separate Event objects.

    Attributes:
        recordedIn: The CreativeWork that captured all or part of this Event.
        isAccessibleForFree: A flag to signal that the item, event, or place is accessible for free.
        aggregateRating: The overall rating, based on a collection of reviews or ratings, of the item.
        eventSchedule: Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable to share a schedule for a series of
      repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly
      gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An [[Event]] that
      is associated with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]] properties. These are instead defined within the associated
      [[Schedule]], this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months
      or seasons.
        director: A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        remainingAttendeeCapacity: The number of attendee places for an event that remain unallocated.
        about: The subject matter of the content.
        subEvent: An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference.
        maximumPhysicalAttendeeCapacity: The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]). 
        workFeatured: A work featured in some event, e.g. exhibited in an ExhibitionEvent.
       Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).
        location: The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        startDate: The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        previousStartDate: Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.
        funder: A person or organization that supports (sponsors) something through some kind of financial contribution.
        maximumVirtualAttendeeCapacity: The maximum virtual attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]). 
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        keywords: Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        translator: Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.
        doorTime: The time admission will commence.
        attendee: A person or organization attending the event.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
        audience: An intended audience, i.e. a group for whom something was created.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        performers: The main performer or performers of the event&#x2014;for example, a presenter, musician, or actor.
        eventStatus: An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.
        actor: An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        superEvent: An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.
        eventAttendanceMode: The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix.
        organizer: An organizer of an Event.
        attendees: A person attending the event.
        subEvents: Events that are a part of this event. For example, a conference event includes many presentations, each subEvents of the conference.
        review: A review of the item.
        performer: A performer at the event&#x2014;for example, a presenter, musician, musical group or actor.
        typicalAgeRange: The typical expected age range, e.g. '7-9', '11-'.
        endDate: The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        contributor: A secondary contributor to the CreativeWork or Event.
        composer: The person or organization who wrote a composition, or who is the composer of a work performed at some event.
        maximumAttendeeCapacity: The total number of individuals that may attend an event or venue.
        workPerformed: A work performed in some event, for example a play performed in a TheaterEvent.
        inLanguage: The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        sponsor: A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    '''
    class_: Literal['https://schema.org/Event'] = Field( # type: ignore
        default='https://schema.org/Event',
        alias='@type',
        serialization_alias='@type'
    )
    recordedIn: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    eventSchedule: Optional[Union['Schedule', List['Schedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    remainingAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    about: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    subEvent: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maximumPhysicalAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    workFeatured: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    location: Optional[Union['VirtualLocation', List['VirtualLocation'], 'PostalAddress', List['PostalAddress'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    previousStartDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maximumVirtualAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    translator: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    doorTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    attendee: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    audience: Optional[Union['Audience', List['Audience']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    performers: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    eventStatus: Optional[Union['EventStatusType', List['EventStatusType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    superEvent: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    eventAttendanceMode: Optional[Union['EventAttendanceModeEnumeration', List['EventAttendanceModeEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    organizer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    attendees: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    subEvents: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    performer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    typicalAgeRange: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    contributor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    composer: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    workPerformed: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    inLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    sponsor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
