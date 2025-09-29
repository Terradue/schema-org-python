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
    from .rating import Rating
    from .defined_term import DefinedTerm
    from .clip import Clip
    from .place import Place
    from .demand import Demand
    from .duration import Duration
    from .grant import Grant
    from .publication_event import PublicationEvent
    from .language import Language
    from .claim import Claim
    from .alignment_object import AlignmentObject
    from .country import Country
    from .comment import Comment
    from .correction_comment import CorrectionComment
    from .audience import Audience
    from .video_object import VideoObject
    from .interaction_counter import InteractionCounter
    from .product import Product
    from .organization import Organization
    from .size_specification import SizeSpecification
    from .audio_object import AudioObject
    from .web_page import WebPage
    from .aggregate_rating import AggregateRating
    from .music_recording import MusicRecording
    from .image_object import ImageObject
    from .quantitative_value import QuantitativeValue
    from .iptc_digital_source_enumeration import IPTCDigitalSourceEnumeration
    from .review import Review
    from .event import Event
    from .item_list import ItemList
    from .media_object import MediaObject
    from .person import Person

class CreativeWork(Thing):
    '''
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.

    Attributes:
        educationalUse: The purpose of a work in the context of education; for example, 'assignment', 'group work'.
        accessMode: The human sensory perceptual system or cognitive faculty through which a person may process or perceive information. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary).
        sdLicense: A license document that applies to this structured data, typically indicated by URL.
        isAccessibleForFree: A flag to signal that the item, event, or place is accessible for free.
        learningResourceType: The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
        creator: The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.
        countryOfOrigin: The country of origin of something, including products as well as creative  works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        assesses: The item being described is intended to assess the competency or learning outcome defined by the referenced term.
        interpretedAsClaim: Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].
        commentCount: The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.
        audio: An embedded audio object.
        reviews: Review of the item.
        contentLocation: The location depicted or described in the content. For example, the location in a photograph or painting.
        publication: A publication event associated with the item.
        license: A license document that applies to this content, typically indicated by URL.
        position: The position of an item in a series or sequence of items.
        contentRating: Official rating of a piece of content&#x2014;for example, 'MPAA PG-13'.
        wordCount: The number of words in the text of the CreativeWork such as an Article, Book, etc.
        interactionStatistic: The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        pattern: A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported.
        accessibilityAPI: Indicates that the resource is compatible with the referenced accessibility API. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary).
        usageInfo: The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]. This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information, e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.

This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses.
        creditText: Text that can be used to credit person(s) and/or organization(s) associated with a published Creative Work.
        workTranslation: A work that is a translation of the content of this work. E.g. 西遊記 has an English workTranslation “Journey to the West”, a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese  translation Tây du ký bình khảo.
        inLanguage: The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        sponsor: A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        awards: Awards won by or for this item.
        discussionUrl: A link to the page containing the comments of the CreativeWork.
        accountablePerson: Specifies the Person that is legally accountable for the CreativeWork.
        conditionsOfAccess: Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]. This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.\
\
For example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ". 
        encodingFormat: Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.

In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.

Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.
        publisherImprint: The publishing division which published the comic.
        accessibilitySummary: A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users" or "short descriptions are present and no long descriptions are needed".
        accessModeSufficient: A list of single or combined accessModes that are sufficient to understand all the intellectual content of a resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).
        sdDatePublished: Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]].
        temporalCoverage: The temporalCoverage of a CreativeWork indicates the period that the content applies to, i.e. that it describes, either as a DateTime or as a textual string indicating a time period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In
      the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate their temporalCoverage in broader terms - textually or via well-known URL.
      Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".

Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated.
        isFamilyFriendly: Indicates whether this content is family friendly.
        acquireLicensePage: Indicates a page documenting how licenses can be purchased or otherwise acquired, for the current item.
        headline: Headline of the article.
        aggregateRating: The overall rating, based on a collection of reviews or ratings, of the item.
        editEIDR: An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing a specific edit / edition for a work of film or television.

For example, the motion picture known as "Ghostbusters" whose [[titleEIDR]] is "10.5240/7EC7-228A-510A-053E-CBB8-J" has several edits, e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".

Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.

        correction: Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]], textually or in another document.
        alternativeHeadline: A secondary title of the CreativeWork.
        isPartOf: Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of.
        version: The version of the CreativeWork embodied by a specified resource.
        translationOfWork: The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the Origin of Species”.
        copyrightHolder: The party holding the legal copyright to the CreativeWork.
        hasPart: Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).
        sourceOrganization: The Organization on whose behalf the creator was working.
        thumbnail: Thumbnail image for an image or video.
        about: The subject matter of the content.
        accessibilityControl: Identifies input methods that are sufficient to fully control the described resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary).
        mentions: Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.
        archivedAt: Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content.
        genre: Genre of the creative work, broadcast channel or group.
        copyrightYear: The year during which the claimed copyright for the CreativeWork was first asserted.
        funder: A person or organization that supports (sponsors) something through some kind of financial contribution.
        timeRequired: Approximate or typical time it usually takes to work with or through the content of this work for the typical or target audience.
        publisher: The publisher of the article in question.
        video: An embedded video object.
        accessibilityFeature: Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary).
        keywords: Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        award: An award won by or for this item.
        translator: Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.
        creativeWorkStatus: The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle.
        expires: Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited, a [[ClaimReview]] fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date, or a [[Certification]] the validity has expired.
        abstract: An abstract is a short description that summarizes a [[CreativeWork]].
        spatialCoverage: The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content. It is a subproperty of
      contentLocation intended primarily for more technical and detailed materials. For example with a Dataset, it indicates
      areas that the dataset describes: a dataset of New York weather would have spatialCoverage which was the place: the state of New York.
        materialExtent: The quantity of the materials being described or an expression of the physical space they occupy.
        accessibilityHazard: A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary).
        associatedMedia: A media object that encodes this CreativeWork. This property is a synonym for encoding.
        contentReferenceTime: The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
        producer: The person or organization who produced the work (e.g. music album, movie, TV/radio series etc.).
        audience: An intended audience, i.e. a group for whom something was created.
        dateCreated: The date on which the CreativeWork was created or the item was added to a DataFeed.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        isBasedOn: A resource from which this work is derived or from which it is a modification or adaptation.
        educationalLevel: The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        mainEntity: Indicates the primary entity described in some page or other CreativeWork.
        thumbnailUrl: A thumbnail image relevant to the Thing.
        author: The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.
        releasedEvent: The place and time the release was issued, expressed as a PublicationEvent.
        recordedAt: The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event.
        schemaVersion: Indicates (by URL or string) a particular version of a schema used in some CreativeWork. This property was created primarily to
    indicate the use of a specific schema.org release, e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```. There may be situations in which other schemas might usefully be referenced this way, e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/``` but this has not been carefully explored in the community.
        material: A material that something is made from, e.g. leather, wool, cotton, paper.
        digitalSourceType: Indicates an IPTCDigitalSourceEnumeration code indicating the nature of the digital source(s) for some [[CreativeWork]].
        exampleOfWork: A creative work that this work is an example/instance/realization/derivation of.
        publishingPrinciples: The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].

While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.

        datePublished: Date of first publication or broadcast. For example the date a [[CreativeWork]] was broadcast or a [[Certification]] was issued.
        temporal: The "temporal" property can be used in cases where more specific properties
(e.g. [[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]]) are not known to be appropriate.
        interactivityType: The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.
        contributor: A secondary contributor to the CreativeWork or Event.
        fileFormat: Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)) of the content, e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry.
        size: A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable. 
        sdPublisher: Indicates the party responsible for generating and publishing the current structured data markup, typically in cases where the structured data is derived automatically from existing published content but published on a different site. For example, student projects and open data initiatives often re-publish existing content with more explicitly structured metadata. The
[[sdPublisher]] property helps make such practices more explicit.
        character: Fictional person connected with a creative work.
        text: The textual content of this CreativeWork.
        educationalAlignment: An alignment to an established educational framework.

This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
        spatial: The "spatial" property can be used in cases when more specific properties
(e.g. [[locationCreated]], [[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.
        workExample: Example/instance/realization/derivation of the concept of this creative work. E.g. the paperback edition, first edition, or e-book.
        citation: A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.
        review: A review of the item.
        maintainer: A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other [[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When [[maintainer]] is applied to a specific version of something e.g. a particular version or packaging of a [[Dataset]], it is always  possible that the upstream source has a different maintainer. The [[isBasedOn]] property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.
      
        teaches: The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.
        typicalAgeRange: The typical expected age range, e.g. '7-9', '11-'.
        editor: Specifies the Person who edited the CreativeWork.
        encoding: A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.
        encodings: A media object that encodes this CreativeWork.
        comment: Comments, typically from users.
        copyrightNotice: Text of a notice appropriate for describing the copyright aspects of this Creative Work, ideally indicating the owner of the copyright for the Work.
        dateModified: The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
        locationCreated: The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.
        provider: The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        isBasedOnUrl: A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.
    '''
    class_: Literal['https://schema.org/CreativeWork'] = Field( # type: ignore
        default='https://schema.org/CreativeWork',
        alias='@type',
        serialization_alias='@type'
    )
    educationalUse: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
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
    sdLicense: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
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
    learningResourceType: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'learningResourceType',
            'https://schema.org/learningResourceType'
        ),
        serialization_alias='https://schema.org/learningResourceType'
    )
    creator: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'creator',
            'https://schema.org/creator'
        ),
        serialization_alias='https://schema.org/creator'
    )
    countryOfOrigin: Optional[Union['Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
    assesses: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'assesses',
            'https://schema.org/assesses'
        ),
        serialization_alias='https://schema.org/assesses'
    )
    interpretedAsClaim: Optional[Union['Claim', List['Claim']]] = Field(
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
    audio: Optional[Union['AudioObject', List['AudioObject'], 'MusicRecording', List['MusicRecording'], 'Clip', List['Clip']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audio',
            'https://schema.org/audio'
        ),
        serialization_alias='https://schema.org/audio'
    )
    reviews: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    contentLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contentLocation',
            'https://schema.org/contentLocation'
        ),
        serialization_alias='https://schema.org/contentLocation'
    )
    publication: Optional[Union['PublicationEvent', List['PublicationEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publication',
            'https://schema.org/publication'
        ),
        serialization_alias='https://schema.org/publication'
    )
    license: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
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
    contentRating: Optional[Union['Rating', List['Rating'], str, List[str]]] = Field(
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
    interactionStatistic: Optional[Union['InteractionCounter', List['InteractionCounter']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic',
            'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic'
    )
    pattern: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
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
    usageInfo: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
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
    workTranslation: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workTranslation',
            'https://schema.org/workTranslation'
        ),
        serialization_alias='https://schema.org/workTranslation'
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
    accountablePerson: Optional[Union['Person', List['Person']]] = Field(
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
    publisherImprint: Optional[Union['Organization', List['Organization']]] = Field(
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
    accessModeSufficient: Optional[Union['ItemList', List['ItemList']]] = Field(
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
    acquireLicensePage: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
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
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
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
    correction: Optional[Union['CorrectionComment', List['CorrectionComment'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
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
    isPartOf: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
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
    translationOfWork: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'translationOfWork',
            'https://schema.org/translationOfWork'
        ),
        serialization_alias='https://schema.org/translationOfWork'
    )
    copyrightHolder: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'copyrightHolder',
            'https://schema.org/copyrightHolder'
        ),
        serialization_alias='https://schema.org/copyrightHolder'
    )
    hasPart: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasPart',
            'https://schema.org/hasPart'
        ),
        serialization_alias='https://schema.org/hasPart'
    )
    sourceOrganization: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sourceOrganization',
            'https://schema.org/sourceOrganization'
        ),
        serialization_alias='https://schema.org/sourceOrganization'
    )
    thumbnail: Optional[Union['ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'thumbnail',
            'https://schema.org/thumbnail'
        ),
        serialization_alias='https://schema.org/thumbnail'
    )
    about: Optional[Union['Thing', List['Thing']]] = Field(
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
    mentions: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mentions',
            'https://schema.org/mentions'
        ),
        serialization_alias='https://schema.org/mentions'
    )
    archivedAt: Optional[Union[HttpUrl, List[HttpUrl], 'WebPage', List['WebPage']]] = Field(
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
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
    timeRequired: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'timeRequired',
            'https://schema.org/timeRequired'
        ),
        serialization_alias='https://schema.org/timeRequired'
    )
    publisher: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publisher',
            'https://schema.org/publisher'
        ),
        serialization_alias='https://schema.org/publisher'
    )
    video: Optional[Union['VideoObject', List['VideoObject'], 'Clip', List['Clip']]] = Field(
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
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
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
    translator: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'translator',
            'https://schema.org/translator'
        ),
        serialization_alias='https://schema.org/translator'
    )
    creativeWorkStatus: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
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
    spatialCoverage: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spatialCoverage',
            'https://schema.org/spatialCoverage'
        ),
        serialization_alias='https://schema.org/spatialCoverage'
    )
    materialExtent: Optional[Union[str, List[str], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    associatedMedia: Optional[Union['MediaObject', List['MediaObject']]] = Field(
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
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    producer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'producer',
            'https://schema.org/producer'
        ),
        serialization_alias='https://schema.org/producer'
    )
    audience: Optional[Union['Audience', List['Audience']]] = Field(
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
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    isBasedOn: Optional[Union['Product', List['Product'], 'CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isBasedOn',
            'https://schema.org/isBasedOn'
        ),
        serialization_alias='https://schema.org/isBasedOn'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel',
            'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel'
    )
    mainEntity: Optional[Union['Thing', List['Thing']]] = Field(
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
    author: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'author',
            'https://schema.org/author'
        ),
        serialization_alias='https://schema.org/author'
    )
    releasedEvent: Optional[Union['PublicationEvent', List['PublicationEvent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releasedEvent',
            'https://schema.org/releasedEvent'
        ),
        serialization_alias='https://schema.org/releasedEvent'
    )
    recordedAt: Optional[Union['Event', List['Event']]] = Field(
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
    material: Optional[Union[str, List[str], 'Product', List['Product'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'material',
            'https://schema.org/material'
        ),
        serialization_alias='https://schema.org/material'
    )
    digitalSourceType: Optional[Union['IPTCDigitalSourceEnumeration', List['IPTCDigitalSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'digitalSourceType',
            'https://schema.org/digitalSourceType'
        ),
        serialization_alias='https://schema.org/digitalSourceType'
    )
    exampleOfWork: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exampleOfWork',
            'https://schema.org/exampleOfWork'
        ),
        serialization_alias='https://schema.org/exampleOfWork'
    )
    publishingPrinciples: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
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
    contributor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
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
    size: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], 'SizeSpecification', List['SizeSpecification'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'size',
            'https://schema.org/size'
        ),
        serialization_alias='https://schema.org/size'
    )
    sdPublisher: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sdPublisher',
            'https://schema.org/sdPublisher'
        ),
        serialization_alias='https://schema.org/sdPublisher'
    )
    character: Optional[Union['Person', List['Person']]] = Field(
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
    educationalAlignment: Optional[Union['AlignmentObject', List['AlignmentObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalAlignment',
            'https://schema.org/educationalAlignment'
        ),
        serialization_alias='https://schema.org/educationalAlignment'
    )
    spatial: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spatial',
            'https://schema.org/spatial'
        ),
        serialization_alias='https://schema.org/spatial'
    )
    workExample: Optional[Union['CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workExample',
            'https://schema.org/workExample'
        ),
        serialization_alias='https://schema.org/workExample'
    )
    citation: Optional[Union[str, List[str], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'citation',
            'https://schema.org/citation'
        ),
        serialization_alias='https://schema.org/citation'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    maintainer: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'maintainer',
            'https://schema.org/maintainer'
        ),
        serialization_alias='https://schema.org/maintainer'
    )
    teaches: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
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
    editor: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'editor',
            'https://schema.org/editor'
        ),
        serialization_alias='https://schema.org/editor'
    )
    encoding: Optional[Union['MediaObject', List['MediaObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encoding',
            'https://schema.org/encoding'
        ),
        serialization_alias='https://schema.org/encoding'
    )
    encodings: Optional[Union['MediaObject', List['MediaObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'encodings',
            'https://schema.org/encodings'
        ),
        serialization_alias='https://schema.org/encodings'
    )
    comment: Optional[Union['Comment', List['Comment']]] = Field(
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
    locationCreated: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'locationCreated',
            'https://schema.org/locationCreated'
        ),
        serialization_alias='https://schema.org/locationCreated'
    )
    provider: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'provider',
            'https://schema.org/provider'
        ),
        serialization_alias='https://schema.org/provider'
    )
    isBasedOnUrl: Optional[Union['Product', List['Product'], 'CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isBasedOnUrl',
            'https://schema.org/isBasedOnUrl'
        ),
        serialization_alias='https://schema.org/isBasedOnUrl'
    )
