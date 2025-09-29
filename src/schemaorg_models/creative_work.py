from __future__ import annotations
from datetime import (
    date,
    datetime
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
    from .language import Language
    from .audio_object import AudioObject
    from .person import Person
    from .image_object import ImageObject
    from .grant import Grant
    from .event import Event
    from .publication_event import PublicationEvent
    from .alignment_object import AlignmentObject
    from .clip import Clip
    from .interaction_counter import InteractionCounter
    from .web_page import WebPage
    from .audience import Audience
    from .iptc_digital_source_enumeration import IPTCDigitalSourceEnumeration
    from .place import Place
    from .defined_term import DefinedTerm
    from .country import Country
    from .size_specification import SizeSpecification
    from .item_list import ItemList
    from .quantitative_value import QuantitativeValue
    from .review import Review
    from .product import Product
    from .video_object import VideoObject
    from .duration import Duration
    from .offer import Offer
    from .claim import Claim
    from .media_object import MediaObject
    from .music_recording import MusicRecording
    from .demand import Demand
    from .aggregate_rating import AggregateRating
    from .comment import Comment
    from .organization import Organization
    from .rating import Rating
    from .correction_comment import CorrectionComment

class CreativeWork(Thing):
    """
The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """
    class_: Literal['https://schema.org/CreativeWork'] = Field( # type: ignore
        default='https://schema.org/CreativeWork',
        alias='@type',
        serialization_alias='@type'
    )
    educationalUse: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalUse',
            'https://schema.org/educationalUse'
        ),
        serialization_alias='https://schema.org/educationalUse'
    )
    accessMode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessMode',
            'https://schema.org/accessMode'
        ),
        serialization_alias='https://schema.org/accessMode'
    )
    sdLicense: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sdLicense',
            'https://schema.org/sdLicense'
        ),
        serialization_alias='https://schema.org/sdLicense'
    )
    isAccessibleForFree: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessibleForFree',
            'https://schema.org/isAccessibleForFree'
        ),
        serialization_alias='https://schema.org/isAccessibleForFree'
    )
    learningResourceType: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'learningResourceType',
            'https://schema.org/learningResourceType'
        ),
        serialization_alias='https://schema.org/learningResourceType'
    )
    creator: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creator',
            'https://schema.org/creator'
        ),
        serialization_alias='https://schema.org/creator'
    )
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
    assesses: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'assesses',
            'https://schema.org/assesses'
        ),
        serialization_alias='https://schema.org/assesses'
    )
    interpretedAsClaim: Optional[Union["Claim", List["Claim"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interpretedAsClaim',
            'https://schema.org/interpretedAsClaim'
        ),
        serialization_alias='https://schema.org/interpretedAsClaim'
    )
    commentCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'commentCount',
            'https://schema.org/commentCount'
        ),
        serialization_alias='https://schema.org/commentCount'
    )
    audio: Optional[Union["AudioObject", List["AudioObject"], "MusicRecording", List["MusicRecording"], "Clip", List["Clip"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audio',
            'https://schema.org/audio'
        ),
        serialization_alias='https://schema.org/audio'
    )
    reviews: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    contentLocation: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentLocation',
            'https://schema.org/contentLocation'
        ),
        serialization_alias='https://schema.org/contentLocation'
    )
    publication: Optional[Union["PublicationEvent", List["PublicationEvent"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publication',
            'https://schema.org/publication'
        ),
        serialization_alias='https://schema.org/publication'
    )
    license: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'license',
            'https://schema.org/license'
        ),
        serialization_alias='https://schema.org/license'
    )
    position: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'position',
            'https://schema.org/position'
        ),
        serialization_alias='https://schema.org/position'
    )
    contentRating: Optional[Union["Rating", List["Rating"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentRating',
            'https://schema.org/contentRating'
        ),
        serialization_alias='https://schema.org/contentRating'
    )
    wordCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'wordCount',
            'https://schema.org/wordCount'
        ),
        serialization_alias='https://schema.org/wordCount'
    )
    interactionStatistic: Optional[Union["InteractionCounter", List["InteractionCounter"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic',
            'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic'
    )
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pattern',
            'https://schema.org/pattern'
        ),
        serialization_alias='https://schema.org/pattern'
    )
    accessibilityAPI: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityAPI',
            'https://schema.org/accessibilityAPI'
        ),
        serialization_alias='https://schema.org/accessibilityAPI'
    )
    usageInfo: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'usageInfo',
            'https://schema.org/usageInfo'
        ),
        serialization_alias='https://schema.org/usageInfo'
    )
    creditText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creditText',
            'https://schema.org/creditText'
        ),
        serialization_alias='https://schema.org/creditText'
    )
    workTranslation: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workTranslation',
            'https://schema.org/workTranslation'
        ),
        serialization_alias='https://schema.org/workTranslation'
    )
    inLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    sponsor: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sponsor',
            'https://schema.org/sponsor'
        ),
        serialization_alias='https://schema.org/sponsor'
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'awards',
            'https://schema.org/awards'
        ),
        serialization_alias='https://schema.org/awards'
    )
    discussionUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'discussionUrl',
            'https://schema.org/discussionUrl'
        ),
        serialization_alias='https://schema.org/discussionUrl'
    )
    accountablePerson: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accountablePerson',
            'https://schema.org/accountablePerson'
        ),
        serialization_alias='https://schema.org/accountablePerson'
    )
    conditionsOfAccess: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'conditionsOfAccess',
            'https://schema.org/conditionsOfAccess'
        ),
        serialization_alias='https://schema.org/conditionsOfAccess'
    )
    encodingFormat: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodingFormat',
            'https://schema.org/encodingFormat'
        ),
        serialization_alias='https://schema.org/encodingFormat'
    )
    publisherImprint: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publisherImprint',
            'https://schema.org/publisherImprint'
        ),
        serialization_alias='https://schema.org/publisherImprint'
    )
    accessibilitySummary: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilitySummary',
            'https://schema.org/accessibilitySummary'
        ),
        serialization_alias='https://schema.org/accessibilitySummary'
    )
    accessModeSufficient: Optional[Union["ItemList", List["ItemList"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessModeSufficient',
            'https://schema.org/accessModeSufficient'
        ),
        serialization_alias='https://schema.org/accessModeSufficient'
    )
    sdDatePublished: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sdDatePublished',
            'https://schema.org/sdDatePublished'
        ),
        serialization_alias='https://schema.org/sdDatePublished'
    )
    temporalCoverage: Optional[Union[datetime, List[datetime], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'temporalCoverage',
            'https://schema.org/temporalCoverage'
        ),
        serialization_alias='https://schema.org/temporalCoverage'
    )
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isFamilyFriendly',
            'https://schema.org/isFamilyFriendly'
        ),
        serialization_alias='https://schema.org/isFamilyFriendly'
    )
    acquireLicensePage: Optional[Union[HttpUrl, List[HttpUrl], "CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acquireLicensePage',
            'https://schema.org/acquireLicensePage'
        ),
        serialization_alias='https://schema.org/acquireLicensePage'
    )
    headline: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'headline',
            'https://schema.org/headline'
        ),
        serialization_alias='https://schema.org/headline'
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    editEIDR: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'editEIDR',
            'https://schema.org/editEIDR'
        ),
        serialization_alias='https://schema.org/editEIDR'
    )
    correction: Optional[Union["CorrectionComment", List["CorrectionComment"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'correction',
            'https://schema.org/correction'
        ),
        serialization_alias='https://schema.org/correction'
    )
    alternativeHeadline: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alternativeHeadline',
            'https://schema.org/alternativeHeadline'
        ),
        serialization_alias='https://schema.org/alternativeHeadline'
    )
    isPartOf: Optional[Union[HttpUrl, List[HttpUrl], "CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isPartOf',
            'https://schema.org/isPartOf'
        ),
        serialization_alias='https://schema.org/isPartOf'
    )
    version: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'version',
            'https://schema.org/version'
        ),
        serialization_alias='https://schema.org/version'
    )
    translationOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'translationOfWork',
            'https://schema.org/translationOfWork'
        ),
        serialization_alias='https://schema.org/translationOfWork'
    )
    copyrightHolder: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightHolder',
            'https://schema.org/copyrightHolder'
        ),
        serialization_alias='https://schema.org/copyrightHolder'
    )
    hasPart: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasPart',
            'https://schema.org/hasPart'
        ),
        serialization_alias='https://schema.org/hasPart'
    )
    sourceOrganization: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sourceOrganization',
            'https://schema.org/sourceOrganization'
        ),
        serialization_alias='https://schema.org/sourceOrganization'
    )
    thumbnail: Optional[Union["ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'thumbnail',
            'https://schema.org/thumbnail'
        ),
        serialization_alias='https://schema.org/thumbnail'
    )
    about: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'about',
            'https://schema.org/about'
        ),
        serialization_alias='https://schema.org/about'
    )
    accessibilityControl: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityControl',
            'https://schema.org/accessibilityControl'
        ),
        serialization_alias='https://schema.org/accessibilityControl'
    )
    mentions: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mentions',
            'https://schema.org/mentions'
        ),
        serialization_alias='https://schema.org/mentions'
    )
    archivedAt: Optional[Union[HttpUrl, List[HttpUrl], "WebPage", List["WebPage"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'archivedAt',
            'https://schema.org/archivedAt'
        ),
        serialization_alias='https://schema.org/archivedAt'
    )
    genre: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    copyrightYear: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightYear',
            'https://schema.org/copyrightYear'
        ),
        serialization_alias='https://schema.org/copyrightYear'
    )
    funder: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
    timeRequired: Optional[Union["Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'timeRequired',
            'https://schema.org/timeRequired'
        ),
        serialization_alias='https://schema.org/timeRequired'
    )
    publisher: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publisher',
            'https://schema.org/publisher'
        ),
        serialization_alias='https://schema.org/publisher'
    )
    video: Optional[Union["VideoObject", List["VideoObject"], "Clip", List["Clip"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'video',
            'https://schema.org/video'
        ),
        serialization_alias='https://schema.org/video'
    )
    accessibilityFeature: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityFeature',
            'https://schema.org/accessibilityFeature'
        ),
        serialization_alias='https://schema.org/accessibilityFeature'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'award',
            'https://schema.org/award'
        ),
        serialization_alias='https://schema.org/award'
    )
    translator: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'translator',
            'https://schema.org/translator'
        ),
        serialization_alias='https://schema.org/translator'
    )
    creativeWorkStatus: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creativeWorkStatus',
            'https://schema.org/creativeWorkStatus'
        ),
        serialization_alias='https://schema.org/creativeWorkStatus'
    )
    expires: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expires',
            'https://schema.org/expires'
        ),
        serialization_alias='https://schema.org/expires'
    )
    abstract: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'abstract',
            'https://schema.org/abstract'
        ),
        serialization_alias='https://schema.org/abstract'
    )
    spatialCoverage: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spatialCoverage',
            'https://schema.org/spatialCoverage'
        ),
        serialization_alias='https://schema.org/spatialCoverage'
    )
    materialExtent: Optional[Union[str, List[str], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'materialExtent',
            'https://schema.org/materialExtent'
        ),
        serialization_alias='https://schema.org/materialExtent'
    )
    accessibilityHazard: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accessibilityHazard',
            'https://schema.org/accessibilityHazard'
        ),
        serialization_alias='https://schema.org/accessibilityHazard'
    )
    associatedMedia: Optional[Union["MediaObject", List["MediaObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'associatedMedia',
            'https://schema.org/associatedMedia'
        ),
        serialization_alias='https://schema.org/associatedMedia'
    )
    contentReferenceTime: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentReferenceTime',
            'https://schema.org/contentReferenceTime'
        ),
        serialization_alias='https://schema.org/contentReferenceTime'
    )
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    producer: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'producer',
            'https://schema.org/producer'
        ),
        serialization_alias='https://schema.org/producer'
    )
    audience: Optional[Union["Audience", List["Audience"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audience',
            'https://schema.org/audience'
        ),
        serialization_alias='https://schema.org/audience'
    )
    dateCreated: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateCreated',
            'https://schema.org/dateCreated'
        ),
        serialization_alias='https://schema.org/dateCreated'
    )
    funding: Optional[Union["Grant", List["Grant"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    isBasedOn: Optional[Union["Product", List["Product"], "CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isBasedOn',
            'https://schema.org/isBasedOn'
        ),
        serialization_alias='https://schema.org/isBasedOn'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel',
            'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel'
    )
    mainEntity: Optional[Union["Thing", List["Thing"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mainEntity',
            'https://schema.org/mainEntity'
        ),
        serialization_alias='https://schema.org/mainEntity'
    )
    thumbnailUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'thumbnailUrl',
            'https://schema.org/thumbnailUrl'
        ),
        serialization_alias='https://schema.org/thumbnailUrl'
    )
    author: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'author',
            'https://schema.org/author'
        ),
        serialization_alias='https://schema.org/author'
    )
    releasedEvent: Optional[Union["PublicationEvent", List["PublicationEvent"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releasedEvent',
            'https://schema.org/releasedEvent'
        ),
        serialization_alias='https://schema.org/releasedEvent'
    )
    recordedAt: Optional[Union["Event", List["Event"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recordedAt',
            'https://schema.org/recordedAt'
        ),
        serialization_alias='https://schema.org/recordedAt'
    )
    schemaVersion: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'schemaVersion',
            'https://schema.org/schemaVersion'
        ),
        serialization_alias='https://schema.org/schemaVersion'
    )
    material: Optional[Union[str, List[str], "Product", List["Product"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'material',
            'https://schema.org/material'
        ),
        serialization_alias='https://schema.org/material'
    )
    digitalSourceType: Optional[Union["IPTCDigitalSourceEnumeration", List["IPTCDigitalSourceEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'digitalSourceType',
            'https://schema.org/digitalSourceType'
        ),
        serialization_alias='https://schema.org/digitalSourceType'
    )
    exampleOfWork: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exampleOfWork',
            'https://schema.org/exampleOfWork'
        ),
        serialization_alias='https://schema.org/exampleOfWork'
    )
    publishingPrinciples: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples',
            'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples'
    )
    datePublished: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePublished',
            'https://schema.org/datePublished'
        ),
        serialization_alias='https://schema.org/datePublished'
    )
    temporal: Optional[Union[str, List[str], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'temporal',
            'https://schema.org/temporal'
        ),
        serialization_alias='https://schema.org/temporal'
    )
    interactivityType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactivityType',
            'https://schema.org/interactivityType'
        ),
        serialization_alias='https://schema.org/interactivityType'
    )
    contributor: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contributor',
            'https://schema.org/contributor'
        ),
        serialization_alias='https://schema.org/contributor'
    )
    fileFormat: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fileFormat',
            'https://schema.org/fileFormat'
        ),
        serialization_alias='https://schema.org/fileFormat'
    )
    size: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str], "SizeSpecification", List["SizeSpecification"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'size',
            'https://schema.org/size'
        ),
        serialization_alias='https://schema.org/size'
    )
    sdPublisher: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sdPublisher',
            'https://schema.org/sdPublisher'
        ),
        serialization_alias='https://schema.org/sdPublisher'
    )
    character: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'character',
            'https://schema.org/character'
        ),
        serialization_alias='https://schema.org/character'
    )
    text: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'text',
            'https://schema.org/text'
        ),
        serialization_alias='https://schema.org/text'
    )
    educationalAlignment: Optional[Union["AlignmentObject", List["AlignmentObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalAlignment',
            'https://schema.org/educationalAlignment'
        ),
        serialization_alias='https://schema.org/educationalAlignment'
    )
    spatial: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spatial',
            'https://schema.org/spatial'
        ),
        serialization_alias='https://schema.org/spatial'
    )
    workExample: Optional[Union["CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workExample',
            'https://schema.org/workExample'
        ),
        serialization_alias='https://schema.org/workExample'
    )
    citation: Optional[Union[str, List[str], "CreativeWork", List["CreativeWork"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'citation',
            'https://schema.org/citation'
        ),
        serialization_alias='https://schema.org/citation'
    )
    review: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    maintainer: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maintainer',
            'https://schema.org/maintainer'
        ),
        serialization_alias='https://schema.org/maintainer'
    )
    teaches: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'teaches',
            'https://schema.org/teaches'
        ),
        serialization_alias='https://schema.org/teaches'
    )
    typicalAgeRange: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typicalAgeRange',
            'https://schema.org/typicalAgeRange'
        ),
        serialization_alias='https://schema.org/typicalAgeRange'
    )
    editor: Optional[Union["Person", List["Person"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'editor',
            'https://schema.org/editor'
        ),
        serialization_alias='https://schema.org/editor'
    )
    encoding: Optional[Union["MediaObject", List["MediaObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encoding',
            'https://schema.org/encoding'
        ),
        serialization_alias='https://schema.org/encoding'
    )
    encodings: Optional[Union["MediaObject", List["MediaObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodings',
            'https://schema.org/encodings'
        ),
        serialization_alias='https://schema.org/encodings'
    )
    comment: Optional[Union["Comment", List["Comment"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'comment',
            'https://schema.org/comment'
        ),
        serialization_alias='https://schema.org/comment'
    )
    copyrightNotice: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightNotice',
            'https://schema.org/copyrightNotice'
        ),
        serialization_alias='https://schema.org/copyrightNotice'
    )
    dateModified: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateModified',
            'https://schema.org/dateModified'
        ),
        serialization_alias='https://schema.org/dateModified'
    )
    locationCreated: Optional[Union["Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'locationCreated',
            'https://schema.org/locationCreated'
        ),
        serialization_alias='https://schema.org/locationCreated'
    )
    provider: Optional[Union["Person", List["Person"], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    isBasedOnUrl: Optional[Union["Product", List["Product"], "CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isBasedOnUrl',
            'https://schema.org/isBasedOnUrl'
        ),
        serialization_alias='https://schema.org/isBasedOnUrl'
    )
