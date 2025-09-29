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
    from .offer import Offer
    from .defined_term import DefinedTerm
    from .virtual_location import VirtualLocation
    from .place import Place
    from .demand import Demand
    from .duration import Duration
    from .grant import Grant
    from .performing_group import PerformingGroup
    from .schedule import Schedule
    from .event_attendance_mode_enumeration import EventAttendanceModeEnumeration
    from .event_status_type import EventStatusType
    from .language import Language
    from .creative_work import CreativeWork
    from .audience import Audience
    from .organization import Organization
    from .person import Person
    from .aggregate_rating import AggregateRating
    from .quantitative_value import QuantitativeValue
    from .review import Review
    from .postal_address import PostalAddress

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
            'recordedIn',
            'https://schema.org/recordedIn'
        ),
        serialization_alias='https://schema.org/recordedIn'
    )
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessibleForFree',
            'https://schema.org/isAccessibleForFree'
        ),
        serialization_alias='https://schema.org/isAccessibleForFree'
    )
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    eventSchedule: Optional[Union['Schedule', List['Schedule']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eventSchedule',
            'https://schema.org/eventSchedule'
        ),
        serialization_alias='https://schema.org/eventSchedule'
    )
    director: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'director',
            'https://schema.org/director'
        ),
        serialization_alias='https://schema.org/director'
    )
    remainingAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'remainingAttendeeCapacity',
            'https://schema.org/remainingAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/remainingAttendeeCapacity'
    )
    about: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'about',
            'https://schema.org/about'
        ),
        serialization_alias='https://schema.org/about'
    )
    subEvent: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subEvent',
            'https://schema.org/subEvent'
        ),
        serialization_alias='https://schema.org/subEvent'
    )
    maximumPhysicalAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumPhysicalAttendeeCapacity',
            'https://schema.org/maximumPhysicalAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/maximumPhysicalAttendeeCapacity'
    )
    workFeatured: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workFeatured',
            'https://schema.org/workFeatured'
        ),
        serialization_alias='https://schema.org/workFeatured'
    )
    location: Optional[Union['VirtualLocation', List['VirtualLocation'], 'PostalAddress', List['PostalAddress'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'location',
            'https://schema.org/location'
        ),
        serialization_alias='https://schema.org/location'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startDate',
            'https://schema.org/startDate'
        ),
        serialization_alias='https://schema.org/startDate'
    )
    previousStartDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'previousStartDate',
            'https://schema.org/previousStartDate'
        ),
        serialization_alias='https://schema.org/previousStartDate'
    )
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
    maximumVirtualAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumVirtualAttendeeCapacity',
            'https://schema.org/maximumVirtualAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/maximumVirtualAttendeeCapacity'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    translator: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'translator',
            'https://schema.org/translator'
        ),
        serialization_alias='https://schema.org/translator'
    )
    doorTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doorTime',
            'https://schema.org/doorTime'
        ),
        serialization_alias='https://schema.org/doorTime'
    )
    attendee: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'attendee',
            'https://schema.org/attendee'
        ),
        serialization_alias='https://schema.org/attendee'
    )
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    audience: Optional[Union['Audience', List['Audience']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audience',
            'https://schema.org/audience'
        ),
        serialization_alias='https://schema.org/audience'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    performers: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'performers',
            'https://schema.org/performers'
        ),
        serialization_alias='https://schema.org/performers'
    )
    eventStatus: Optional[Union['EventStatusType', List['EventStatusType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eventStatus',
            'https://schema.org/eventStatus'
        ),
        serialization_alias='https://schema.org/eventStatus'
    )
    actor: Optional[Union['Person', List['Person'], 'PerformingGroup', List['PerformingGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actor',
            'https://schema.org/actor'
        ),
        serialization_alias='https://schema.org/actor'
    )
    superEvent: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'superEvent',
            'https://schema.org/superEvent'
        ),
        serialization_alias='https://schema.org/superEvent'
    )
    eventAttendanceMode: Optional[Union['EventAttendanceModeEnumeration', List['EventAttendanceModeEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eventAttendanceMode',
            'https://schema.org/eventAttendanceMode'
        ),
        serialization_alias='https://schema.org/eventAttendanceMode'
    )
    organizer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'organizer',
            'https://schema.org/organizer'
        ),
        serialization_alias='https://schema.org/organizer'
    )
    attendees: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'attendees',
            'https://schema.org/attendees'
        ),
        serialization_alias='https://schema.org/attendees'
    )
    subEvents: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subEvents',
            'https://schema.org/subEvents'
        ),
        serialization_alias='https://schema.org/subEvents'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    performer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'performer',
            'https://schema.org/performer'
        ),
        serialization_alias='https://schema.org/performer'
    )
    typicalAgeRange: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typicalAgeRange',
            'https://schema.org/typicalAgeRange'
        ),
        serialization_alias='https://schema.org/typicalAgeRange'
    )
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endDate',
            'https://schema.org/endDate'
        ),
        serialization_alias='https://schema.org/endDate'
    )
    contributor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contributor',
            'https://schema.org/contributor'
        ),
        serialization_alias='https://schema.org/contributor'
    )
    composer: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'composer',
            'https://schema.org/composer'
        ),
        serialization_alias='https://schema.org/composer'
    )
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maximumAttendeeCapacity',
            'https://schema.org/maximumAttendeeCapacity'
        ),
        serialization_alias='https://schema.org/maximumAttendeeCapacity'
    )
    workPerformed: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workPerformed',
            'https://schema.org/workPerformed'
        ),
        serialization_alias='https://schema.org/workPerformed'
    )
    inLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    sponsor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sponsor',
            'https://schema.org/sponsor'
        ),
        serialization_alias='https://schema.org/sponsor'
    )
