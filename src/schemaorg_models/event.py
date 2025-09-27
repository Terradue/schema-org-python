from typing import List, Literal, Optional, Union
from datetime import date, datetime, time
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.thing import Thing

from schemaorg_models.person import Person
from schemaorg_models.thing import Thing
from schemaorg_models.place import Place

class Event(Thing):
    """
Upcoming or past event associated with this place, organization, or action.
    """
    class_: Literal['https://schema.org/Event'] = Field(default='https://schema.org/Event', alias='class', serialization_alias='class') # type: ignore
    recordedIn: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(default=None, validation_alias=AliasChoices('recordedIn', 'https://schema.org/recordedIn'), serialization_alias='https://schema.org/recordedIn')
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('isAccessibleForFree', 'https://schema.org/isAccessibleForFree'), serialization_alias='https://schema.org/isAccessibleForFree')
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(default=None, validation_alias=AliasChoices('aggregateRating', 'https://schema.org/aggregateRating'), serialization_alias='https://schema.org/aggregateRating')
    eventSchedule: Optional[Union["Schedule", List["Schedule"]]] = Field(default=None, validation_alias=AliasChoices('eventSchedule', 'https://schema.org/eventSchedule'), serialization_alias='https://schema.org/eventSchedule')
    director: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('director', 'https://schema.org/director'), serialization_alias='https://schema.org/director')
    remainingAttendeeCapacity: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('remainingAttendeeCapacity', 'https://schema.org/remainingAttendeeCapacity'), serialization_alias='https://schema.org/remainingAttendeeCapacity')
    about: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('about', 'https://schema.org/about'), serialization_alias='https://schema.org/about')
    subEvent: Optional[Union["Event", List["Event"]]] = Field(default=None, validation_alias=AliasChoices('subEvent', 'https://schema.org/subEvent'), serialization_alias='https://schema.org/subEvent')
    maximumPhysicalAttendeeCapacity: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('maximumPhysicalAttendeeCapacity', 'https://schema.org/maximumPhysicalAttendeeCapacity'), serialization_alias='https://schema.org/maximumPhysicalAttendeeCapacity')
    workFeatured: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(default=None, validation_alias=AliasChoices('workFeatured', 'https://schema.org/workFeatured'), serialization_alias='https://schema.org/workFeatured')
    location: Optional[Union["VirtualLocation", List["VirtualLocation"], "PostalAddress", List["PostalAddress"], str, List[str], Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('location', 'https://schema.org/location'), serialization_alias='https://schema.org/location')
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'), serialization_alias='https://schema.org/startDate')
    previousStartDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('previousStartDate', 'https://schema.org/previousStartDate'), serialization_alias='https://schema.org/previousStartDate')
    funder: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('funder', 'https://schema.org/funder'), serialization_alias='https://schema.org/funder')
    maximumVirtualAttendeeCapacity: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('maximumVirtualAttendeeCapacity', 'https://schema.org/maximumVirtualAttendeeCapacity'), serialization_alias='https://schema.org/maximumVirtualAttendeeCapacity')
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('duration', 'https://schema.org/duration'), serialization_alias='https://schema.org/duration')
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None, validation_alias=AliasChoices('keywords', 'https://schema.org/keywords'), serialization_alias='https://schema.org/keywords')
    @field_serializer('keywords')
    def keywords2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    translator: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('translator', 'https://schema.org/translator'), serialization_alias='https://schema.org/translator')
    doorTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('doorTime', 'https://schema.org/doorTime'), serialization_alias='https://schema.org/doorTime')
    attendee: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('attendee', 'https://schema.org/attendee'), serialization_alias='https://schema.org/attendee')
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(default=None, validation_alias=AliasChoices('offers', 'https://schema.org/offers'), serialization_alias='https://schema.org/offers')
    audience: Optional[Union["Audience", List["Audience"]]] = Field(default=None, validation_alias=AliasChoices('audience', 'https://schema.org/audience'), serialization_alias='https://schema.org/audience')
    funding: Optional[Union["Grant", List["Grant"]]] = Field(default=None, validation_alias=AliasChoices('funding', 'https://schema.org/funding'), serialization_alias='https://schema.org/funding')
    performers: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('performers', 'https://schema.org/performers'), serialization_alias='https://schema.org/performers')
    eventStatus: Optional[Union["EventStatusType", List["EventStatusType"]]] = Field(default=None, validation_alias=AliasChoices('eventStatus', 'https://schema.org/eventStatus'), serialization_alias='https://schema.org/eventStatus')
    actor: Optional[Union[Person, List[Person], "PerformingGroup", List["PerformingGroup"]]] = Field(default=None, validation_alias=AliasChoices('actor', 'https://schema.org/actor'), serialization_alias='https://schema.org/actor')
    superEvent: Optional[Union["Event", List["Event"]]] = Field(default=None, validation_alias=AliasChoices('superEvent', 'https://schema.org/superEvent'), serialization_alias='https://schema.org/superEvent')
    eventAttendanceMode: Optional[Union["EventAttendanceModeEnumeration", List["EventAttendanceModeEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('eventAttendanceMode', 'https://schema.org/eventAttendanceMode'), serialization_alias='https://schema.org/eventAttendanceMode')
    organizer: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('organizer', 'https://schema.org/organizer'), serialization_alias='https://schema.org/organizer')
    attendees: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('attendees', 'https://schema.org/attendees'), serialization_alias='https://schema.org/attendees')
    subEvents: Optional[Union["Event", List["Event"]]] = Field(default=None, validation_alias=AliasChoices('subEvents', 'https://schema.org/subEvents'), serialization_alias='https://schema.org/subEvents')
    review: Optional[Union["Review", List["Review"]]] = Field(default=None, validation_alias=AliasChoices('review', 'https://schema.org/review'), serialization_alias='https://schema.org/review')
    performer: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('performer', 'https://schema.org/performer'), serialization_alias='https://schema.org/performer')
    typicalAgeRange: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('typicalAgeRange', 'https://schema.org/typicalAgeRange'), serialization_alias='https://schema.org/typicalAgeRange')
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None, validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'), serialization_alias='https://schema.org/endDate')
    contributor: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('contributor', 'https://schema.org/contributor'), serialization_alias='https://schema.org/contributor')
    composer: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('composer', 'https://schema.org/composer'), serialization_alias='https://schema.org/composer')
    maximumAttendeeCapacity: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('maximumAttendeeCapacity', 'https://schema.org/maximumAttendeeCapacity'), serialization_alias='https://schema.org/maximumAttendeeCapacity')
    workPerformed: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(default=None, validation_alias=AliasChoices('workPerformed', 'https://schema.org/workPerformed'), serialization_alias='https://schema.org/workPerformed')
    inLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(default=None, validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'), serialization_alias='https://schema.org/inLanguage')
    sponsor: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'), serialization_alias='https://schema.org/sponsor')
