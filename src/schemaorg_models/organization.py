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
    from .language import Language
    from .shipping_service import ShippingService
    from .ownership_info import OwnershipInfo
    from .image_object import ImageObject
    from .geo_shape import GeoShape
    from .brand import Brand
    from .merchant_return_policy import MerchantReturnPolicy
    from .loan_or_credit import LoanOrCredit
    from .virtual_location import VirtualLocation
    from .payment_method import PaymentMethod
    from .event import Event
    from .nonprofit_type import NonprofitType
    from .member_program import MemberProgram
    from .creative_work import CreativeWork
    from .administrative_area import AdministrativeArea
    from .article import Article
    from .defined_term import DefinedTerm
    from .interaction_counter import InteractionCounter
    from .product import Product
    from .certification import Certification
    from .offer import Offer
    from .demand import Demand
    from .review import Review
    from .aggregate_rating import AggregateRating
    from .postal_address import PostalAddress
    from .person import Person
    from .product_return_policy import ProductReturnPolicy
    from .contact_point import ContactPoint
    from .place import Place
    from .offer_catalog import OfferCatalog
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .grant import Grant
    from .program_membership import ProgramMembership
    from .member_program_tier import MemberProgramTier
    from .quantitative_value import QuantitativeValue
    from .about_page import AboutPage

class Organization(Thing):
    '''
    An organization such as a school, NGO, corporation, club, etc.

    Attributes:
        knowsAbout: Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions.
        employees: People working for this organization.
        iso6523Code: An organization identifier as defined in [ISO 6523(-1)](https://en.wikipedia.org/wiki/ISO/IEC_6523). The identifier should be in the `XXXX:YYYYYY:ZZZ` or `XXXX:YYYYYY`format. Where `XXXX` is a 4 digit _ICD_ (International Code Designator), `YYYYYY` is an _OID_ (Organization Identifier) with all formatting characters (dots, dashes, spaces) removed with a maximal length of 35 characters, and `ZZZ` is an optional OPI (Organization Part Identifier) with a maximum length of 35 characters. The various components (ICD, OID, OPI) are joined with a colon character (ASCII `0x3a`). Note that many existing organization identifiers defined as attributes like [leiCode](https://schema.org/leiCode) (`0199`), [duns](https://schema.org/duns) (`0060`) or [GLN](https://schema.org/globalLocationNumber) (`0088`) can be expressed using ISO-6523. If possible, ISO-6523 codes should be preferred to populating [vatID](https://schema.org/vatID) or [taxID](https://schema.org/taxID), as ISO identifiers are less ambiguous.
        telephone: The telephone number.
        acceptedPaymentMethod: The payment method(s) that are accepted in general by an organization, or for some specific demand or offer.
        brand: The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        member: A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.
        contactPoints: A contact point for a person or organization.
        review: A review of the item.
        hasMemberProgram: MemberProgram offered by an Organization, for example an eCommerce merchant or an airline.
        hasShippingService: Specification of a shipping service offered by the organization.
        publishingPrinciples: The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].

While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.

        department: A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.
        isicV4: The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        duns: The Dun & Bradstreet DUNS number for identifying an organization or business person.
        hasPOS: Points-of-Sales operated by the organization or person.
        skills: A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is either claimed by a person, an organization or desired or required to fulfill a role or to work in an occupation.
        subOrganization: A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific 'department' property.
        hasMerchantReturnPolicy: Specifies a MerchantReturnPolicy that may be applicable.
        ownershipFundingInfo: For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence.   Note that the [[funder]] is also available and can be used to make basic funder information machine-readable.
        knowsLanguage: Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).
        makesOffer: A pointer to products or services offered by the organization or person.
        faxNumber: The fax number.
        ethicsPolicy: Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic and publishing practices, or of a [[Restaurant]], a page describing food source policies. In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.
        globalLocationNumber: The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        sponsor: A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        event: Upcoming or past event associated with this place, organization, or action.
        owns: Products owned by the organization or person.
        reviews: Review of the item.
        nonprofitStatus: nonprofitStatus indicates the legal status of a non-profit organization in its primary place of business.
        aggregateRating: The overall rating, based on a collection of reviews or ratings, of the item.
        dissolutionDate: The date that this organization was dissolved.
        areaServed: The geographic area where a service or offered item is provided.
        memberOf: An Organization (or ProgramMembership) to which this Person or Organization belongs.
        contactPoint: A contact point for a person or organization.
        founder: A person or organization who founded this organization.
        interactionStatistic: The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        legalAddress: The legal address of an organization which acts as the officially registered address used for legal and tax purposes. The legal address can be different from the place of operations of a business and other addresses can be part of an organization.
        vatID: The Value-added Tax ID of the organization or person.
        parentOrganization: The larger organization that this organization is a [[subOrganization]] of, if any.
        awards: Awards won by or for this item.
        location: The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        actionableFeedbackPolicy: For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.
        legalRepresentative: One or multiple persons who represent this organization legally such as CEO or sole administrator.
        serviceArea: The geographic area where the service is provided.
        hasOfferCatalog: Indicates an OfferCatalog listing for this Organization, Person, or Service.
        hasCertification: Certification information about a product, organization, service, place, or person.
        correctionsPolicy: For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.
        members: A member of this organization.
        keywords: Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        hasProductReturnPolicy: Indicates a ProductReturnPolicy that may be applicable.
        logo: An associated logo.
        numberOfEmployees: The number of employees in an organization, e.g. business.
        email: Email address.
        seeks: A pointer to products or services sought by the organization or person (demand).
        legalName: The official name of the organization, e.g. the registered company name.
        hasCredential: A credential awarded to the Person or Organization.
        alumni: Alumni of an organization.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        funder: A person or organization that supports (sponsors) something through some kind of financial contribution.
        agentInteractionStatistic: The number of completed interactions for this entity, in a particular role (the 'agent'), in a particular action (indicated in the statistic), and in a particular context (i.e. interactionService).
        naics: The North American Industry Classification System (NAICS) code for a particular organization or business person.
        slogan: A slogan or motto associated with the item.
        foundingDate: The date that this organization was founded.
        diversityPolicy: Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]. For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.
        founders: A person who founded this organization.
        award: An award won by or for this item.
        foundingLocation: The place where the Organization was founded.
        unnamedSourcesPolicy: For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about policy on use of unnamed sources and the decision process required.
        leiCode: An organization identifier that uniquely identifies a legal entity as defined in ISO 17442.
        address: Physical address of the item.
        events: Upcoming or past events associated with this place or organization.
        employee: Someone working for this organization.
        taxID: The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.
        hasGS1DigitalLink: The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>)  should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly.
        diversityStaffingReport: For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.
        companyRegistration: The official registration number of a business including the organization that issued it such as Company House or Chamber of Commerce.
    '''
    class_: Literal['https://schema.org/Organization'] = Field( # type: ignore
        default='https://schema.org/Organization',
        alias='@type',
        serialization_alias='@type'
    )
    knowsAbout: Optional[Union[str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsAbout',
            'https://schema.org/knowsAbout'
        ),
        serialization_alias='https://schema.org/knowsAbout'
    )
    employees: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'employees',
            'https://schema.org/employees'
        ),
        serialization_alias='https://schema.org/employees'
    )
    iso6523Code: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'iso6523Code',
            'https://schema.org/iso6523Code'
        ),
        serialization_alias='https://schema.org/iso6523Code'
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'telephone',
            'https://schema.org/telephone'
        ),
        serialization_alias='https://schema.org/telephone'
    )
    acceptedPaymentMethod: Optional[Union[str, List[str], 'PaymentMethod', List['PaymentMethod'], 'LoanOrCredit', List['LoanOrCredit']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod',
            'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod'
    )
    brand: Optional[Union['Organization', List['Organization'], 'Brand', List['Brand']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'brand',
            'https://schema.org/brand'
        ),
        serialization_alias='https://schema.org/brand'
    )
    member: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'member',
            'https://schema.org/member'
        ),
        serialization_alias='https://schema.org/member'
    )
    contactPoints: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoints',
            'https://schema.org/contactPoints'
        ),
        serialization_alias='https://schema.org/contactPoints'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    hasMemberProgram: Optional[Union['MemberProgram', List['MemberProgram']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMemberProgram',
            'https://schema.org/hasMemberProgram'
        ),
        serialization_alias='https://schema.org/hasMemberProgram'
    )
    hasShippingService: Optional[Union['ShippingService', List['ShippingService']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasShippingService',
            'https://schema.org/hasShippingService'
        ),
        serialization_alias='https://schema.org/hasShippingService'
    )
    publishingPrinciples: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples',
            'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples'
    )
    department: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'department',
            'https://schema.org/department'
        ),
        serialization_alias='https://schema.org/department'
    )
    isicV4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isicV4',
            'https://schema.org/isicV4'
        ),
        serialization_alias='https://schema.org/isicV4'
    )
    duns: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duns',
            'https://schema.org/duns'
        ),
        serialization_alias='https://schema.org/duns'
    )
    hasPOS: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasPOS',
            'https://schema.org/hasPOS'
        ),
        serialization_alias='https://schema.org/hasPOS'
    )
    skills: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'skills',
            'https://schema.org/skills'
        ),
        serialization_alias='https://schema.org/skills'
    )
    subOrganization: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subOrganization',
            'https://schema.org/subOrganization'
        ),
        serialization_alias='https://schema.org/subOrganization'
    )
    hasMerchantReturnPolicy: Optional[Union['MerchantReturnPolicy', List['MerchantReturnPolicy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy',
            'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy'
    )
    ownershipFundingInfo: Optional[Union[str, List[str], 'CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl], 'AboutPage', List['AboutPage']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ownershipFundingInfo',
            'https://schema.org/ownershipFundingInfo'
        ),
        serialization_alias='https://schema.org/ownershipFundingInfo'
    )
    knowsLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsLanguage',
            'https://schema.org/knowsLanguage'
        ),
        serialization_alias='https://schema.org/knowsLanguage'
    )
    makesOffer: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'makesOffer',
            'https://schema.org/makesOffer'
        ),
        serialization_alias='https://schema.org/makesOffer'
    )
    faxNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'faxNumber',
            'https://schema.org/faxNumber'
        ),
        serialization_alias='https://schema.org/faxNumber'
    )
    ethicsPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ethicsPolicy',
            'https://schema.org/ethicsPolicy'
        ),
        serialization_alias='https://schema.org/ethicsPolicy'
    )
    globalLocationNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'globalLocationNumber',
            'https://schema.org/globalLocationNumber'
        ),
        serialization_alias='https://schema.org/globalLocationNumber'
    )
    sponsor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sponsor',
            'https://schema.org/sponsor'
        ),
        serialization_alias='https://schema.org/sponsor'
    )
    event: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
    owns: Optional[Union['Product', List['Product'], 'OwnershipInfo', List['OwnershipInfo']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'owns',
            'https://schema.org/owns'
        ),
        serialization_alias='https://schema.org/owns'
    )
    reviews: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    nonprofitStatus: Optional[Union['NonprofitType', List['NonprofitType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonprofitStatus',
            'https://schema.org/nonprofitStatus'
        ),
        serialization_alias='https://schema.org/nonprofitStatus'
    )
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    dissolutionDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dissolutionDate',
            'https://schema.org/dissolutionDate'
        ),
        serialization_alias='https://schema.org/dissolutionDate'
    )
    areaServed: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'AdministrativeArea', List['AdministrativeArea'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
    memberOf: Optional[Union['Organization', List['Organization'], 'MemberProgramTier', List['MemberProgramTier'], 'ProgramMembership', List['ProgramMembership']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'memberOf',
            'https://schema.org/memberOf'
        ),
        serialization_alias='https://schema.org/memberOf'
    )
    contactPoint: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint',
            'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint'
    )
    founder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'founder',
            'https://schema.org/founder'
        ),
        serialization_alias='https://schema.org/founder'
    )
    interactionStatistic: Optional[Union['InteractionCounter', List['InteractionCounter']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic',
            'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic'
    )
    legalAddress: Optional[Union['PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalAddress',
            'https://schema.org/legalAddress'
        ),
        serialization_alias='https://schema.org/legalAddress'
    )
    vatID: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vatID',
            'https://schema.org/vatID'
        ),
        serialization_alias='https://schema.org/vatID'
    )
    parentOrganization: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentOrganization',
            'https://schema.org/parentOrganization'
        ),
        serialization_alias='https://schema.org/parentOrganization'
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'awards',
            'https://schema.org/awards'
        ),
        serialization_alias='https://schema.org/awards'
    )
    location: Optional[Union['VirtualLocation', List['VirtualLocation'], 'PostalAddress', List['PostalAddress'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'location',
            'https://schema.org/location'
        ),
        serialization_alias='https://schema.org/location'
    )
    actionableFeedbackPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionableFeedbackPolicy',
            'https://schema.org/actionableFeedbackPolicy'
        ),
        serialization_alias='https://schema.org/actionableFeedbackPolicy'
    )
    legalRepresentative: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalRepresentative',
            'https://schema.org/legalRepresentative'
        ),
        serialization_alias='https://schema.org/legalRepresentative'
    )
    serviceArea: Optional[Union['AdministrativeArea', List['AdministrativeArea'], 'GeoShape', List['GeoShape'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceArea',
            'https://schema.org/serviceArea'
        ),
        serialization_alias='https://schema.org/serviceArea'
    )
    hasOfferCatalog: Optional[Union['OfferCatalog', List['OfferCatalog']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOfferCatalog',
            'https://schema.org/hasOfferCatalog'
        ),
        serialization_alias='https://schema.org/hasOfferCatalog'
    )
    hasCertification: Optional[Union['Certification', List['Certification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification',
            'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification'
    )
    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'correctionsPolicy',
            'https://schema.org/correctionsPolicy'
        ),
        serialization_alias='https://schema.org/correctionsPolicy'
    )
    members: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'members',
            'https://schema.org/members'
        ),
        serialization_alias='https://schema.org/members'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    hasProductReturnPolicy: Optional[Union['ProductReturnPolicy', List['ProductReturnPolicy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasProductReturnPolicy',
            'https://schema.org/hasProductReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasProductReturnPolicy'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    numberOfEmployees: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfEmployees',
            'https://schema.org/numberOfEmployees'
        ),
        serialization_alias='https://schema.org/numberOfEmployees'
    )
    email: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'email',
            'https://schema.org/email'
        ),
        serialization_alias='https://schema.org/email'
    )
    seeks: Optional[Union['Demand', List['Demand']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seeks',
            'https://schema.org/seeks'
        ),
        serialization_alias='https://schema.org/seeks'
    )
    legalName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalName',
            'https://schema.org/legalName'
        ),
        serialization_alias='https://schema.org/legalName'
    )
    hasCredential: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCredential',
            'https://schema.org/hasCredential'
        ),
        serialization_alias='https://schema.org/hasCredential'
    )
    alumni: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alumni',
            'https://schema.org/alumni'
        ),
        serialization_alias='https://schema.org/alumni'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
    agentInteractionStatistic: Optional[Union['InteractionCounter', List['InteractionCounter']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'agentInteractionStatistic',
            'https://schema.org/agentInteractionStatistic'
        ),
        serialization_alias='https://schema.org/agentInteractionStatistic'
    )
    naics: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'naics',
            'https://schema.org/naics'
        ),
        serialization_alias='https://schema.org/naics'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'slogan',
            'https://schema.org/slogan'
        ),
        serialization_alias='https://schema.org/slogan'
    )
    foundingDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foundingDate',
            'https://schema.org/foundingDate'
        ),
        serialization_alias='https://schema.org/foundingDate'
    )
    diversityPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityPolicy',
            'https://schema.org/diversityPolicy'
        ),
        serialization_alias='https://schema.org/diversityPolicy'
    )
    founders: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'founders',
            'https://schema.org/founders'
        ),
        serialization_alias='https://schema.org/founders'
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'award',
            'https://schema.org/award'
        ),
        serialization_alias='https://schema.org/award'
    )
    foundingLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foundingLocation',
            'https://schema.org/foundingLocation'
        ),
        serialization_alias='https://schema.org/foundingLocation'
    )
    unnamedSourcesPolicy: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unnamedSourcesPolicy',
            'https://schema.org/unnamedSourcesPolicy'
        ),
        serialization_alias='https://schema.org/unnamedSourcesPolicy'
    )
    leiCode: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'leiCode',
            'https://schema.org/leiCode'
        ),
        serialization_alias='https://schema.org/leiCode'
    )
    address: Optional[Union[str, List[str], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'address',
            'https://schema.org/address'
        ),
        serialization_alias='https://schema.org/address'
    )
    events: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'events',
            'https://schema.org/events'
        ),
        serialization_alias='https://schema.org/events'
    )
    employee: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'employee',
            'https://schema.org/employee'
        ),
        serialization_alias='https://schema.org/employee'
    )
    taxID: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'taxID',
            'https://schema.org/taxID'
        ),
        serialization_alias='https://schema.org/taxID'
    )
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink',
            'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink'
    )
    diversityStaffingReport: Optional[Union['Article', List['Article'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityStaffingReport',
            'https://schema.org/diversityStaffingReport'
        ),
        serialization_alias='https://schema.org/diversityStaffingReport'
    )
    companyRegistration: Optional[Union['Certification', List['Certification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'companyRegistration',
            'https://schema.org/companyRegistration'
        ),
        serialization_alias='https://schema.org/companyRegistration'
    )
