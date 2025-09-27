from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.web_content import WebContent
from schemaorg_models.thing import Thing
from schemaorg_models.observation import Observation
from schemaorg_models.local_business import LocalBusiness
from schemaorg_models.civic_structure import CivicStructure

class SpecialAnnouncement(CreativeWork):
    """
A SpecialAnnouncement combines a simple date-stamped textual information update
      with contextualized Web links and other structured data.  It represents an information update made by a
      locally-oriented organization, for example schools, pharmacies, healthcare providers,  community groups, police,
      local government.

For work in progress guidelines on Coronavirus-related markup see [this doc](https://docs.google.com/document/d/14ikaGCKxo50rRM7nvKSlbUpjyIk2WMQd3IkB1lItlrM/edit#).

The motivating scenario for SpecialAnnouncement is the [Coronavirus pandemic](https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic), and the initial vocabulary is oriented to this urgent situation. Schema.org
expect to improve the markup iteratively as it is deployed and as feedback emerges from use. In addition to our
usual [Github entry](https://github.com/schemaorg/schemaorg/issues/2490), feedback comments can also be provided in [this document](https://docs.google.com/document/d/1fpdFFxk8s87CWwACs53SGkYv3aafSxz_DTtOQxMrBJQ/edit#).


While this schema is designed to communicate urgent crisis-related information, it is not the same as an emergency warning technology like [CAP](https://en.wikipedia.org/wiki/Common_Alerting_Protocol), although there may be overlaps. The intent is to cover
the kinds of everyday practical information being posted to existing websites during an emergency situation.

Several kinds of information can be provided:

We encourage the provision of "name", "text", "datePosted", "expires" (if appropriate), "category" and
"url" as a simple baseline. It is important to provide a value for "category" where possible, most ideally as a well known
URL from Wikipedia or Wikidata. In the case of the 2019-2020 Coronavirus pandemic, this should be "https://en.wikipedia.org/w/index.php?title=2019-20\\_coronavirus\\_pandemic" or "https://www.wikidata.org/wiki/Q81068910".

For many of the possible properties, values can either be simple links or an inline description, depending on whether a summary is available. For a link, provide just the URL of the appropriate page as the property's value. For an inline description, use a [[WebContent]] type, and provide the url as a property of that, alongside at least a simple "[[text]]" summary of the page. It is
unlikely that a single SpecialAnnouncement will need all of the possible properties simultaneously.

We expect that in many cases the page referenced might contain more specialized structured data, e.g. contact info, [[openingHours]], [[Event]], [[FAQPage]] etc. By linking to those pages from a [[SpecialAnnouncement]] you can help make it clearer that the events are related to the situation (e.g. Coronavirus) indicated by the [[category]] property of the [[SpecialAnnouncement]].

Many [[SpecialAnnouncement]]s will relate to particular regions and to identifiable local organizations. Use [[spatialCoverage]] for the region, and [[announcementLocation]] to indicate specific [[LocalBusiness]]es and [[CivicStructure]]s. If the announcement affects both a particular region and a specific location (for example, a library closure that serves an entire region), use both [[spatialCoverage]] and [[announcementLocation]].

The [[about]] property can be used to indicate entities that are the focus of the announcement. We now recommend using [[about]] only
for representing non-location entities (e.g. a [[Course]] or a [[RadioStation]]). For places, use [[announcementLocation]] and [[spatialCoverage]]. Consumers of this markup should be aware that the initial design encouraged the use of [[about]] for locations too.

The basic content of [[SpecialAnnouncement]] is similar to that of an [RSS](https://en.wikipedia.org/wiki/RSS) or [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)) feed. For publishers without such feeds, basic feed-like information can be shared by posting
[[SpecialAnnouncement]] updates in a page, e.g. using JSON-LD. For sites with Atom/RSS functionality, you can point to a feed
with the [[webFeed]] property. This can be a simple URL, or an inline [[DataFeed]] object, with [[encodingFormat]] providing
media type information, e.g. "application/rss+xml" or "application/atom+xml".

    """
    class_: Literal['https://schema.org/SpecialAnnouncement'] = Field(default='https://schema.org/SpecialAnnouncement', alias='@type', serialization_alias='@type') # type: ignore
    travelBans: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('travelBans', 'https://schema.org/travelBans'), serialization_alias='https://schema.org/travelBans')
    @field_serializer('travelBans')
    def travelBans2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    quarantineGuidelines: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('quarantineGuidelines', 'https://schema.org/quarantineGuidelines'), serialization_alias='https://schema.org/quarantineGuidelines')
    @field_serializer('quarantineGuidelines')
    def quarantineGuidelines2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('datePosted', 'https://schema.org/datePosted'), serialization_alias='https://schema.org/datePosted')
    newsUpdatesAndGuidelines: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('newsUpdatesAndGuidelines', 'https://schema.org/newsUpdatesAndGuidelines'), serialization_alias='https://schema.org/newsUpdatesAndGuidelines')
    @field_serializer('newsUpdatesAndGuidelines')
    def newsUpdatesAndGuidelines2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    publicTransportClosuresInfo: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('publicTransportClosuresInfo', 'https://schema.org/publicTransportClosuresInfo'), serialization_alias='https://schema.org/publicTransportClosuresInfo')
    @field_serializer('publicTransportClosuresInfo')
    def publicTransportClosuresInfo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    governmentBenefitsInfo: Optional[Union["GovernmentService", List["GovernmentService"]]] = Field(default=None, validation_alias=AliasChoices('governmentBenefitsInfo', 'https://schema.org/governmentBenefitsInfo'), serialization_alias='https://schema.org/governmentBenefitsInfo')
    gettingTestedInfo: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('gettingTestedInfo', 'https://schema.org/gettingTestedInfo'), serialization_alias='https://schema.org/gettingTestedInfo')
    @field_serializer('gettingTestedInfo')
    def gettingTestedInfo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    diseasePreventionInfo: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('diseasePreventionInfo', 'https://schema.org/diseasePreventionInfo'), serialization_alias='https://schema.org/diseasePreventionInfo')
    @field_serializer('diseasePreventionInfo')
    def diseasePreventionInfo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('category', 'https://schema.org/category'), serialization_alias='https://schema.org/category')
    @field_serializer('category')
    def category2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    schoolClosuresInfo: Optional[Union[HttpUrl, List[HttpUrl], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('schoolClosuresInfo', 'https://schema.org/schoolClosuresInfo'), serialization_alias='https://schema.org/schoolClosuresInfo')
    @field_serializer('schoolClosuresInfo')
    def schoolClosuresInfo2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    diseaseSpreadStatistics: Optional[Union[Observation, List[Observation], HttpUrl, List[HttpUrl], "Dataset", List["Dataset"], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('diseaseSpreadStatistics', 'https://schema.org/diseaseSpreadStatistics'), serialization_alias='https://schema.org/diseaseSpreadStatistics')
    @field_serializer('diseaseSpreadStatistics')
    def diseaseSpreadStatistics2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    announcementLocation: Optional[Union[LocalBusiness, List[LocalBusiness], CivicStructure, List[CivicStructure]]] = Field(default=None, validation_alias=AliasChoices('announcementLocation', 'https://schema.org/announcementLocation'), serialization_alias='https://schema.org/announcementLocation')
    webFeed: Optional[Union["DataFeed", List["DataFeed"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('webFeed', 'https://schema.org/webFeed'), serialization_alias='https://schema.org/webFeed')
    @field_serializer('webFeed')
    def webFeed2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

