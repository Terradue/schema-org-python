from __future__ import annotations

from .thing import Thing    

from datetime import (
    date
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
from schemaorg_models.person import Person
from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.place import Place
from schemaorg_models.event import Event
from schemaorg_models.product import Product

class Organization(Thing):
    """
An organization such as a school, NGO, corporation, club, etc.
    """
    class_: Literal['https://schema.org/Organization'] = Field( # type: ignore
        default='https://schema.org/Organization',
        alias='@type',
        serialization_alias='@type'
    )
    knowsAbout: Optional[Union[str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsAbout',
            'https://schema.org/knowsAbout'
        ),
        serialization_alias='https://schema.org/knowsAbout'
    )
    employees: Optional[Union[Person, List[Person]]] = Field(
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
    acceptedPaymentMethod: Optional[Union[str, List[str], "PaymentMethod", List["PaymentMethod"], "LoanOrCredit", List["LoanOrCredit"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod',
            'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod'
    )
    brand: Optional[Union["Organization", List["Organization"], "Brand", List["Brand"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'brand',
            'https://schema.org/brand'
        ),
        serialization_alias='https://schema.org/brand'
    )
    member: Optional[Union[Person, List[Person], "Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'member',
            'https://schema.org/member'
        ),
        serialization_alias='https://schema.org/member'
    )
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoints',
            'https://schema.org/contactPoints'
        ),
        serialization_alias='https://schema.org/contactPoints'
    )
    review: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    hasMemberProgram: Optional[Union["MemberProgram", List["MemberProgram"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMemberProgram',
            'https://schema.org/hasMemberProgram'
        ),
        serialization_alias='https://schema.org/hasMemberProgram'
    )
    hasShippingService: Optional[Union["ShippingService", List["ShippingService"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasShippingService',
            'https://schema.org/hasShippingService'
        ),
        serialization_alias='https://schema.org/hasShippingService'
    )
    publishingPrinciples: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'publishingPrinciples',
            'https://schema.org/publishingPrinciples'
        ),
        serialization_alias='https://schema.org/publishingPrinciples'
    )
    department: Optional[Union["Organization", List["Organization"]]] = Field(
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
    hasPOS: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasPOS',
            'https://schema.org/hasPOS'
        ),
        serialization_alias='https://schema.org/hasPOS'
    )
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'skills',
            'https://schema.org/skills'
        ),
        serialization_alias='https://schema.org/skills'
    )
    subOrganization: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subOrganization',
            'https://schema.org/subOrganization'
        ),
        serialization_alias='https://schema.org/subOrganization'
    )
    hasMerchantReturnPolicy: Optional[Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy',
            'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy'
    )
    ownershipFundingInfo: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl], "AboutPage", List["AboutPage"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ownershipFundingInfo',
            'https://schema.org/ownershipFundingInfo'
        ),
        serialization_alias='https://schema.org/ownershipFundingInfo'
    )
    knowsLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knowsLanguage',
            'https://schema.org/knowsLanguage'
        ),
        serialization_alias='https://schema.org/knowsLanguage'
    )
    makesOffer: Optional[Union["Offer", List["Offer"]]] = Field(
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
    ethicsPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
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
    sponsor: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sponsor',
            'https://schema.org/sponsor'
        ),
        serialization_alias='https://schema.org/sponsor'
    )
    event: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'event',
            'https://schema.org/event'
        ),
        serialization_alias='https://schema.org/event'
    )
    owns: Optional[Union[Product, List[Product], "OwnershipInfo", List["OwnershipInfo"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'owns',
            'https://schema.org/owns'
        ),
        serialization_alias='https://schema.org/owns'
    )
    reviews: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    nonprofitStatus: Optional[Union["NonprofitType", List["NonprofitType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nonprofitStatus',
            'https://schema.org/nonprofitStatus'
        ),
        serialization_alias='https://schema.org/nonprofitStatus'
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(
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
    areaServed: Optional[Union["GeoShape", List["GeoShape"], str, List[str], "AdministrativeArea", List["AdministrativeArea"], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
    memberOf: Optional[Union["Organization", List["Organization"], "MemberProgramTier", List["MemberProgramTier"], "ProgramMembership", List["ProgramMembership"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'memberOf',
            'https://schema.org/memberOf'
        ),
        serialization_alias='https://schema.org/memberOf'
    )
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'contactPoint',
            'https://schema.org/contactPoint'
        ),
        serialization_alias='https://schema.org/contactPoint'
    )
    founder: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'founder',
            'https://schema.org/founder'
        ),
        serialization_alias='https://schema.org/founder'
    )
    interactionStatistic: Optional[Union["InteractionCounter", List["InteractionCounter"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interactionStatistic',
            'https://schema.org/interactionStatistic'
        ),
        serialization_alias='https://schema.org/interactionStatistic'
    )
    legalAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = Field(
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
    parentOrganization: Optional[Union["Organization", List["Organization"]]] = Field(
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
    location: Optional[Union["VirtualLocation", List["VirtualLocation"], "PostalAddress", List["PostalAddress"], str, List[str], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'location',
            'https://schema.org/location'
        ),
        serialization_alias='https://schema.org/location'
    )
    actionableFeedbackPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionableFeedbackPolicy',
            'https://schema.org/actionableFeedbackPolicy'
        ),
        serialization_alias='https://schema.org/actionableFeedbackPolicy'
    )
    legalRepresentative: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legalRepresentative',
            'https://schema.org/legalRepresentative'
        ),
        serialization_alias='https://schema.org/legalRepresentative'
    )
    serviceArea: Optional[Union["AdministrativeArea", List["AdministrativeArea"], "GeoShape", List["GeoShape"], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serviceArea',
            'https://schema.org/serviceArea'
        ),
        serialization_alias='https://schema.org/serviceArea'
    )
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasOfferCatalog',
            'https://schema.org/hasOfferCatalog'
        ),
        serialization_alias='https://schema.org/hasOfferCatalog'
    )
    hasCertification: Optional[Union["Certification", List["Certification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification',
            'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification'
    )
    correctionsPolicy: Optional[Union[HttpUrl, List[HttpUrl], CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'correctionsPolicy',
            'https://schema.org/correctionsPolicy'
        ),
        serialization_alias='https://schema.org/correctionsPolicy'
    )
    members: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'members',
            'https://schema.org/members'
        ),
        serialization_alias='https://schema.org/members'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    hasProductReturnPolicy: Optional[Union["ProductReturnPolicy", List["ProductReturnPolicy"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasProductReturnPolicy',
            'https://schema.org/hasProductReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasProductReturnPolicy'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    numberOfEmployees: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
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
    seeks: Optional[Union["Demand", List["Demand"]]] = Field(
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
    hasCredential: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCredential',
            'https://schema.org/hasCredential'
        ),
        serialization_alias='https://schema.org/hasCredential'
    )
    alumni: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'alumni',
            'https://schema.org/alumni'
        ),
        serialization_alias='https://schema.org/alumni'
    )
    funding: Optional[Union["Grant", List["Grant"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    funder: Optional[Union["Organization", List["Organization"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funder',
            'https://schema.org/funder'
        ),
        serialization_alias='https://schema.org/funder'
    )
    agentInteractionStatistic: Optional[Union["InteractionCounter", List["InteractionCounter"]]] = Field(
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
    diversityPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityPolicy',
            'https://schema.org/diversityPolicy'
        ),
        serialization_alias='https://schema.org/diversityPolicy'
    )
    founders: Optional[Union[Person, List[Person]]] = Field(
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
    foundingLocation: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'foundingLocation',
            'https://schema.org/foundingLocation'
        ),
        serialization_alias='https://schema.org/foundingLocation'
    )
    unnamedSourcesPolicy: Optional[Union[CreativeWork, List[CreativeWork], HttpUrl, List[HttpUrl]]] = Field(
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
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'address',
            'https://schema.org/address'
        ),
        serialization_alias='https://schema.org/address'
    )
    events: Optional[Union[Event, List[Event]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'events',
            'https://schema.org/events'
        ),
        serialization_alias='https://schema.org/events'
    )
    employee: Optional[Union[Person, List[Person]]] = Field(
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
    diversityStaffingReport: Optional[Union["Article", List["Article"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diversityStaffingReport',
            'https://schema.org/diversityStaffingReport'
        ),
        serialization_alias='https://schema.org/diversityStaffingReport'
    )
    companyRegistration: Optional[Union["Certification", List["Certification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'companyRegistration',
            'https://schema.org/companyRegistration'
        ),
        serialization_alias='https://schema.org/companyRegistration'
    )
