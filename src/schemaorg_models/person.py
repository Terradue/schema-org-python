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
    from .country import Country
    from .monetary_amount import MonetaryAmount
    from .language import Language
    from .ownership_info import OwnershipInfo
    from .educational_organization import EducationalOrganization
    from .brand import Brand
    from .organization import Organization
    from .distance import Distance
    from .event import Event
    from .structured_value import StructuredValue
    from .creative_work import CreativeWork
    from .defined_term import DefinedTerm
    from .interaction_counter import InteractionCounter
    from .demand import Demand
    from .product import Product
    from .certification import Certification
    from .offer import Offer
    from .occupation import Occupation
    from .price_specification import PriceSpecification
    from .postal_address import PostalAddress
    from .contact_point import ContactPoint
    from .place import Place
    from .offer_catalog import OfferCatalog
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .grant import Grant
    from .program_membership import ProgramMembership
    from .mass import Mass
    from .gender_type import GenderType
    from .member_program_tier import MemberProgramTier
    from .quantitative_value import QuantitativeValue

class Person(Thing):
    '''
    A person (alive, dead, undead, or fictional).

    Attributes:
        knowsLanguage: Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).
        gender: Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who are not a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed".
        faxNumber: The fax number.
        globalLocationNumber: The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        sponsor: A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        deathPlace: The place where the person died.
        follows: The most generic uni-directional social relation.
        sibling: A sibling of the person.
        hasOfferCatalog: Indicates an OfferCatalog listing for this Organization, Person, or Service.
        hasCertification: Certification information about a product, organization, service, place, or person.
        homeLocation: A contact location for a person's residence.
        alumniOf: An organization that the person is an alumni of.
        familyName: Family name. In the U.S., the last name of a Person.
        birthDate: Date of birth.
        owns: Products owned by the organization or person.
        memberOf: An Organization (or ProgramMembership) to which this Person or Organization belongs.
        interactionStatistic: The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        vatID: The Value-added Tax ID of the organization or person.
        awards: Awards won by or for this item.
        jobTitle: The job title of the person (for example, Financial Manager).
        funder: A person or organization that supports (sponsors) something through some kind of financial contribution.
        deathDate: Date of death.
        spouse: The person's spouse.
        honorificPrefix: An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.
        email: Email address.
        netWorth: The total financial value of the person as calculated by subtracting the total value of liabilities from the total value of assets.
        siblings: A sibling of the person.
        colleagues: A colleague of the person.
        seeks: A pointer to products or services sought by the organization or person (demand).
        nationality: Nationality of the person.
        hasCredential: A credential awarded to the Person or Organization.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        agentInteractionStatistic: The number of completed interactions for this entity, in a particular role (the 'agent'), in a particular action (indicated in the statistic), and in a particular context (i.e. interactionService).
        naics: The North American Industry Classification System (NAICS) code for a particular organization or business person.
        colleague: A colleague of the person.
        givenName: Given name. In the U.S., the first name of a Person.
        worksFor: Organizations that the person works for.
        additionalName: An additional name for a Person, can be used for a middle name.
        hasOccupation: The Person's occupation. For past professions, use Role for expressing dates.
        knows: The most generic bi-directional social/work relation.
        award: An award won by or for this item.
        parents: A parents of the person.
        address: Physical address of the item.
        height: The height of the item.
        taxID: The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.
        weight: The weight of the product or person.
        children: A child of the person.
        performerIn: Event that this person is a performer or participant in.
        pronouns: A short string listing or describing pronouns for a person. Typically the person concerned is the best authority as pronouns are a critical part of personal identity and expression. Publishers and consumers of this information are reminded to treat this data responsibly, take country-specific laws related to gender expression into account, and be wary of out-of-date data and drawing unwarranted inferences about the person being described.

In English, formulations such as "they/them", "she/her", and "he/him" are commonly used online and can also be used here. We do not intend to enumerate all possible micro-syntaxes in all languages. More structured and well-defined external values for pronouns can be referenced using the [[StructuredValue]] or [[DefinedTerm]] values.

        knowsAbout: Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions.
        telephone: The telephone number.
        callSign: A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        brand: The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        contactPoints: A contact point for a person or organization.
        workLocation: A contact location for a person's place of work.
        makesOffer: A pointer to products or services offered by the organization or person.
        birthPlace: The place where the person was born.
        publishingPrinciples: The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].

While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.

        isicV4: The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        honorificSuffix: An honorific suffix following a Person's name such as M.D./PhD/MSCSW.
        duns: The Dun & Bradstreet DUNS number for identifying an organization or business person.
        hasPOS: Points-of-Sales operated by the organization or person.
        skills: A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is either claimed by a person, an organization or desired or required to fulfill a role or to work in an occupation.
        relatedTo: The most generic familial relation.
        contactPoint: A contact point for a person or organization.
        affiliation: An organization that this person is affiliated with. For example, a school/university, a club, or a team.
        parent: A parent of this person.
    '''
    class_: Literal['https://schema.org/Person'] = Field( # type: ignore
        default='https://schema.org/Person',
        alias='@type',
        serialization_alias='@type'
    )
    knowsLanguage: Optional[Union[str, List[str], 'Language', List['Language']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsLanguage',
            'https://schema.org/knowsLanguage'
        ),
        serialization_alias='https://schema.org/knowsLanguage'
    )
    gender: Optional[Union['GenderType', List['GenderType'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gender',
            'https://schema.org/gender'
        ),
        serialization_alias='https://schema.org/gender'
    )
    faxNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'faxNumber',
            'https://schema.org/faxNumber'
        ),
        serialization_alias='https://schema.org/faxNumber'
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
    deathPlace: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deathPlace',
            'https://schema.org/deathPlace'
        ),
        serialization_alias='https://schema.org/deathPlace'
    )
    follows: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'follows',
            'https://schema.org/follows'
        ),
        serialization_alias='https://schema.org/follows'
    )
    sibling: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sibling',
            'https://schema.org/sibling'
        ),
        serialization_alias='https://schema.org/sibling'
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
    homeLocation: Optional[Union['Place', List['Place'], 'ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'homeLocation',
            'https://schema.org/homeLocation'
        ),
        serialization_alias='https://schema.org/homeLocation'
    )
    alumniOf: Optional[Union['Organization', List['Organization'], 'EducationalOrganization', List['EducationalOrganization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alumniOf',
            'https://schema.org/alumniOf'
        ),
        serialization_alias='https://schema.org/alumniOf'
    )
    familyName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'familyName',
            'https://schema.org/familyName'
        ),
        serialization_alias='https://schema.org/familyName'
    )
    birthDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'birthDate',
            'https://schema.org/birthDate'
        ),
        serialization_alias='https://schema.org/birthDate'
    )
    owns: Optional[Union['Product', List['Product'], 'OwnershipInfo', List['OwnershipInfo']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'owns',
            'https://schema.org/owns'
        ),
        serialization_alias='https://schema.org/owns'
    )
    memberOf: Optional[Union['Organization', List['Organization'], 'MemberProgramTier', List['MemberProgramTier'], 'ProgramMembership', List['ProgramMembership']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'memberOf',
            'https://schema.org/memberOf'
        ),
        serialization_alias='https://schema.org/memberOf'
    )
    interactionStatistic: Optional[Union['InteractionCounter', List['InteractionCounter']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic',
            'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic'
    )
    vatID: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vatID',
            'https://schema.org/vatID'
        ),
        serialization_alias='https://schema.org/vatID'
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'awards',
            'https://schema.org/awards'
        ),
        serialization_alias='https://schema.org/awards'
    )
    jobTitle: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jobTitle',
            'https://schema.org/jobTitle'
        ),
        serialization_alias='https://schema.org/jobTitle'
    )
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
    deathDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deathDate',
            'https://schema.org/deathDate'
        ),
        serialization_alias='https://schema.org/deathDate'
    )
    spouse: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spouse',
            'https://schema.org/spouse'
        ),
        serialization_alias='https://schema.org/spouse'
    )
    honorificPrefix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'honorificPrefix',
            'https://schema.org/honorificPrefix'
        ),
        serialization_alias='https://schema.org/honorificPrefix'
    )
    email: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'email',
            'https://schema.org/email'
        ),
        serialization_alias='https://schema.org/email'
    )
    netWorth: Optional[Union['PriceSpecification', List['PriceSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'netWorth',
            'https://schema.org/netWorth'
        ),
        serialization_alias='https://schema.org/netWorth'
    )
    siblings: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'siblings',
            'https://schema.org/siblings'
        ),
        serialization_alias='https://schema.org/siblings'
    )
    colleagues: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'colleagues',
            'https://schema.org/colleagues'
        ),
        serialization_alias='https://schema.org/colleagues'
    )
    seeks: Optional[Union['Demand', List['Demand']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seeks',
            'https://schema.org/seeks'
        ),
        serialization_alias='https://schema.org/seeks'
    )
    nationality: Optional[Union['Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nationality',
            'https://schema.org/nationality'
        ),
        serialization_alias='https://schema.org/nationality'
    )
    hasCredential: Optional[Union['EducationalOccupationalCredential', List['EducationalOccupationalCredential']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCredential',
            'https://schema.org/hasCredential'
        ),
        serialization_alias='https://schema.org/hasCredential'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
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
    colleague: Optional[Union['Person', List['Person'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'colleague',
            'https://schema.org/colleague'
        ),
        serialization_alias='https://schema.org/colleague'
    )
    givenName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'givenName',
            'https://schema.org/givenName'
        ),
        serialization_alias='https://schema.org/givenName'
    )
    worksFor: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'worksFor',
            'https://schema.org/worksFor'
        ),
        serialization_alias='https://schema.org/worksFor'
    )
    additionalName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalName',
            'https://schema.org/additionalName'
        ),
        serialization_alias='https://schema.org/additionalName'
    )
    hasOccupation: Optional[Union['Occupation', List['Occupation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOccupation',
            'https://schema.org/hasOccupation'
        ),
        serialization_alias='https://schema.org/hasOccupation'
    )
    knows: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knows',
            'https://schema.org/knows'
        ),
        serialization_alias='https://schema.org/knows'
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'award',
            'https://schema.org/award'
        ),
        serialization_alias='https://schema.org/award'
    )
    parents: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parents',
            'https://schema.org/parents'
        ),
        serialization_alias='https://schema.org/parents'
    )
    address: Optional[Union[str, List[str], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'address',
            'https://schema.org/address'
        ),
        serialization_alias='https://schema.org/address'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
    taxID: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'taxID',
            'https://schema.org/taxID'
        ),
        serialization_alias='https://schema.org/taxID'
    )
    weight: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    children: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'children',
            'https://schema.org/children'
        ),
        serialization_alias='https://schema.org/children'
    )
    performerIn: Optional[Union['Event', List['Event']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'performerIn',
            'https://schema.org/performerIn'
        ),
        serialization_alias='https://schema.org/performerIn'
    )
    pronouns: Optional[Union[str, List[str], 'StructuredValue', List['StructuredValue'], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pronouns',
            'https://schema.org/pronouns'
        ),
        serialization_alias='https://schema.org/pronouns'
    )
    knowsAbout: Optional[Union[str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsAbout',
            'https://schema.org/knowsAbout'
        ),
        serialization_alias='https://schema.org/knowsAbout'
    )
    telephone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'telephone',
            'https://schema.org/telephone'
        ),
        serialization_alias='https://schema.org/telephone'
    )
    callSign: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'callSign',
            'https://schema.org/callSign'
        ),
        serialization_alias='https://schema.org/callSign'
    )
    brand: Optional[Union['Organization', List['Organization'], 'Brand', List['Brand']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'brand',
            'https://schema.org/brand'
        ),
        serialization_alias='https://schema.org/brand'
    )
    contactPoints: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoints',
            'https://schema.org/contactPoints'
        ),
        serialization_alias='https://schema.org/contactPoints'
    )
    workLocation: Optional[Union['ContactPoint', List['ContactPoint'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'workLocation',
            'https://schema.org/workLocation'
        ),
        serialization_alias='https://schema.org/workLocation'
    )
    makesOffer: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'makesOffer',
            'https://schema.org/makesOffer'
        ),
        serialization_alias='https://schema.org/makesOffer'
    )
    birthPlace: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'birthPlace',
            'https://schema.org/birthPlace'
        ),
        serialization_alias='https://schema.org/birthPlace'
    )
    publishingPrinciples: Optional[Union['CreativeWork', List['CreativeWork'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples',
            'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples'
    )
    isicV4: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isicV4',
            'https://schema.org/isicV4'
        ),
        serialization_alias='https://schema.org/isicV4'
    )
    honorificSuffix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'honorificSuffix',
            'https://schema.org/honorificSuffix'
        ),
        serialization_alias='https://schema.org/honorificSuffix'
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
    relatedTo: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'relatedTo',
            'https://schema.org/relatedTo'
        ),
        serialization_alias='https://schema.org/relatedTo'
    )
    contactPoint: Optional[Union['ContactPoint', List['ContactPoint']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint',
            'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint'
    )
    affiliation: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'affiliation',
            'https://schema.org/affiliation'
        ),
        serialization_alias='https://schema.org/affiliation'
    )
    parent: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parent',
            'https://schema.org/parent'
        ),
        serialization_alias='https://schema.org/parent'
    )
