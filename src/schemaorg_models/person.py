from typing import List, Literal, Optional, Union
from datetime import date
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.thing import Thing

from schemaorg_models.thing import Thing

class Person(Thing):
    """
A person (alive, dead, undead, or fictional).
    """
    type_: Literal['https://schema.org/Person'] = Field(default='https://schema.org/Person', alias='@type', serialization_alias='@type') # type: ignore
    knowsLanguage: Optional[Union[str, List[str], "Language", List["Language"]]] = Field(default=None, validation_alias=AliasChoices('knowsLanguage', 'https://schema.org/knowsLanguage'), serialization_alias='https://schema.org/knowsLanguage')
    gender: Optional[Union["GenderType", List["GenderType"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('gender', 'https://schema.org/gender'), serialization_alias='https://schema.org/gender')
    faxNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('faxNumber', 'https://schema.org/faxNumber'), serialization_alias='https://schema.org/faxNumber')
    globalLocationNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('globalLocationNumber', 'https://schema.org/globalLocationNumber'), serialization_alias='https://schema.org/globalLocationNumber')
    sponsor: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'), serialization_alias='https://schema.org/sponsor')
    deathPlace: Optional[Union["Place", List["Place"]]] = Field(default=None, validation_alias=AliasChoices('deathPlace', 'https://schema.org/deathPlace'), serialization_alias='https://schema.org/deathPlace')
    follows: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('follows', 'https://schema.org/follows'), serialization_alias='https://schema.org/follows')
    sibling: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('sibling', 'https://schema.org/sibling'), serialization_alias='https://schema.org/sibling')
    hasOfferCatalog: Optional[Union["OfferCatalog", List["OfferCatalog"]]] = Field(default=None, validation_alias=AliasChoices('hasOfferCatalog', 'https://schema.org/hasOfferCatalog'), serialization_alias='https://schema.org/hasOfferCatalog')
    hasCertification: Optional[Union["Certification", List["Certification"]]] = Field(default=None, validation_alias=AliasChoices('hasCertification', 'https://schema.org/hasCertification'), serialization_alias='https://schema.org/hasCertification')
    homeLocation: Optional[Union["Place", List["Place"], "ContactPoint", List["ContactPoint"]]] = Field(default=None, validation_alias=AliasChoices('homeLocation', 'https://schema.org/homeLocation'), serialization_alias='https://schema.org/homeLocation')
    alumniOf: Optional[Union["Organization", List["Organization"], "EducationalOrganization", List["EducationalOrganization"]]] = Field(default=None, validation_alias=AliasChoices('alumniOf', 'https://schema.org/alumniOf'), serialization_alias='https://schema.org/alumniOf')
    familyName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('familyName', 'https://schema.org/familyName'), serialization_alias='https://schema.org/familyName')
    birthDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('birthDate', 'https://schema.org/birthDate'), serialization_alias='https://schema.org/birthDate')
    owns: Optional[Union["Product", List["Product"], "OwnershipInfo", List["OwnershipInfo"]]] = Field(default=None, validation_alias=AliasChoices('owns', 'https://schema.org/owns'), serialization_alias='https://schema.org/owns')
    memberOf: Optional[Union["Organization", List["Organization"], "MemberProgramTier", List["MemberProgramTier"], "ProgramMembership", List["ProgramMembership"]]] = Field(default=None, validation_alias=AliasChoices('memberOf', 'https://schema.org/memberOf'), serialization_alias='https://schema.org/memberOf')
    interactionStatistic: Optional[Union["InteractionCounter", List["InteractionCounter"]]] = Field(default=None, validation_alias=AliasChoices('interactionStatistic', 'https://schema.org/interactionStatistic'), serialization_alias='https://schema.org/interactionStatistic')
    vatID: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('vatID', 'https://schema.org/vatID'), serialization_alias='https://schema.org/vatID')
    awards: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('awards', 'https://schema.org/awards'), serialization_alias='https://schema.org/awards')
    jobTitle: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('jobTitle', 'https://schema.org/jobTitle'), serialization_alias='https://schema.org/jobTitle')
    funder: Optional[Union["Organization", List["Organization"], "Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('funder', 'https://schema.org/funder'), serialization_alias='https://schema.org/funder')
    deathDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('deathDate', 'https://schema.org/deathDate'), serialization_alias='https://schema.org/deathDate')
    spouse: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('spouse', 'https://schema.org/spouse'), serialization_alias='https://schema.org/spouse')
    honorificPrefix: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('honorificPrefix', 'https://schema.org/honorificPrefix'), serialization_alias='https://schema.org/honorificPrefix')
    email: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('email', 'https://schema.org/email'), serialization_alias='https://schema.org/email')
    netWorth: Optional[Union["PriceSpecification", List["PriceSpecification"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('netWorth', 'https://schema.org/netWorth'), serialization_alias='https://schema.org/netWorth')
    siblings: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('siblings', 'https://schema.org/siblings'), serialization_alias='https://schema.org/siblings')
    colleagues: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('colleagues', 'https://schema.org/colleagues'), serialization_alias='https://schema.org/colleagues')
    seeks: Optional[Union["Demand", List["Demand"]]] = Field(default=None, validation_alias=AliasChoices('seeks', 'https://schema.org/seeks'), serialization_alias='https://schema.org/seeks')
    nationality: Optional[Union["Country", List["Country"]]] = Field(default=None, validation_alias=AliasChoices('nationality', 'https://schema.org/nationality'), serialization_alias='https://schema.org/nationality')
    hasCredential: Optional[Union["EducationalOccupationalCredential", List["EducationalOccupationalCredential"]]] = Field(default=None, validation_alias=AliasChoices('hasCredential', 'https://schema.org/hasCredential'), serialization_alias='https://schema.org/hasCredential')
    funding: Optional[Union["Grant", List["Grant"]]] = Field(default=None, validation_alias=AliasChoices('funding', 'https://schema.org/funding'), serialization_alias='https://schema.org/funding')
    agentInteractionStatistic: Optional[Union["InteractionCounter", List["InteractionCounter"]]] = Field(default=None, validation_alias=AliasChoices('agentInteractionStatistic', 'https://schema.org/agentInteractionStatistic'), serialization_alias='https://schema.org/agentInteractionStatistic')
    naics: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('naics', 'https://schema.org/naics'), serialization_alias='https://schema.org/naics')
    colleague: Optional[Union["Person", List["Person"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('colleague', 'https://schema.org/colleague'), serialization_alias='https://schema.org/colleague')
    @field_serializer('colleague')
    def colleague2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    givenName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('givenName', 'https://schema.org/givenName'), serialization_alias='https://schema.org/givenName')
    worksFor: Optional[Union["Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('worksFor', 'https://schema.org/worksFor'), serialization_alias='https://schema.org/worksFor')
    additionalName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('additionalName', 'https://schema.org/additionalName'), serialization_alias='https://schema.org/additionalName')
    hasOccupation: Optional[Union["Occupation", List["Occupation"]]] = Field(default=None, validation_alias=AliasChoices('hasOccupation', 'https://schema.org/hasOccupation'), serialization_alias='https://schema.org/hasOccupation')
    knows: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('knows', 'https://schema.org/knows'), serialization_alias='https://schema.org/knows')
    award: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('award', 'https://schema.org/award'), serialization_alias='https://schema.org/award')
    parents: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('parents', 'https://schema.org/parents'), serialization_alias='https://schema.org/parents')
    address: Optional[Union[str, List[str], "PostalAddress", List["PostalAddress"]]] = Field(default=None, validation_alias=AliasChoices('address', 'https://schema.org/address'), serialization_alias='https://schema.org/address')
    height: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('height', 'https://schema.org/height'), serialization_alias='https://schema.org/height')
    taxID: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('taxID', 'https://schema.org/taxID'), serialization_alias='https://schema.org/taxID')
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Mass", List["Mass"]]] = Field(default=None, validation_alias=AliasChoices('weight', 'https://schema.org/weight'), serialization_alias='https://schema.org/weight')
    children: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('children', 'https://schema.org/children'), serialization_alias='https://schema.org/children')
    performerIn: Optional[Union["Event", List["Event"]]] = Field(default=None, validation_alias=AliasChoices('performerIn', 'https://schema.org/performerIn'), serialization_alias='https://schema.org/performerIn')
    pronouns: Optional[Union[str, List[str], "StructuredValue", List["StructuredValue"], "DefinedTerm", List["DefinedTerm"]]] = Field(default=None, validation_alias=AliasChoices('pronouns', 'https://schema.org/pronouns'), serialization_alias='https://schema.org/pronouns')
    knowsAbout: Optional[Union[str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('knowsAbout', 'https://schema.org/knowsAbout'), serialization_alias='https://schema.org/knowsAbout')
    @field_serializer('knowsAbout')
    def knowsAbout2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    telephone: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('telephone', 'https://schema.org/telephone'), serialization_alias='https://schema.org/telephone')
    callSign: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('callSign', 'https://schema.org/callSign'), serialization_alias='https://schema.org/callSign')
    brand: Optional[Union["Organization", List["Organization"], "Brand", List["Brand"]]] = Field(default=None, validation_alias=AliasChoices('brand', 'https://schema.org/brand'), serialization_alias='https://schema.org/brand')
    contactPoints: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(default=None, validation_alias=AliasChoices('contactPoints', 'https://schema.org/contactPoints'), serialization_alias='https://schema.org/contactPoints')
    workLocation: Optional[Union["ContactPoint", List["ContactPoint"], "Place", List["Place"]]] = Field(default=None, validation_alias=AliasChoices('workLocation', 'https://schema.org/workLocation'), serialization_alias='https://schema.org/workLocation')
    makesOffer: Optional[Union["Offer", List["Offer"]]] = Field(default=None, validation_alias=AliasChoices('makesOffer', 'https://schema.org/makesOffer'), serialization_alias='https://schema.org/makesOffer')
    birthPlace: Optional[Union["Place", List["Place"]]] = Field(default=None, validation_alias=AliasChoices('birthPlace', 'https://schema.org/birthPlace'), serialization_alias='https://schema.org/birthPlace')
    publishingPrinciples: Optional[Union["CreativeWork", List["CreativeWork"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('publishingPrinciples', 'https://schema.org/publishingPrinciples'), serialization_alias='https://schema.org/publishingPrinciples')
    @field_serializer('publishingPrinciples')
    def publishingPrinciples2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    isicV4: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('isicV4', 'https://schema.org/isicV4'), serialization_alias='https://schema.org/isicV4')
    honorificSuffix: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('honorificSuffix', 'https://schema.org/honorificSuffix'), serialization_alias='https://schema.org/honorificSuffix')
    duns: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('duns', 'https://schema.org/duns'), serialization_alias='https://schema.org/duns')
    hasPOS: Optional[Union["Place", List["Place"]]] = Field(default=None, validation_alias=AliasChoices('hasPOS', 'https://schema.org/hasPOS'), serialization_alias='https://schema.org/hasPOS')
    skills: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('skills', 'https://schema.org/skills'), serialization_alias='https://schema.org/skills')
    relatedTo: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('relatedTo', 'https://schema.org/relatedTo'), serialization_alias='https://schema.org/relatedTo')
    contactPoint: Optional[Union["ContactPoint", List["ContactPoint"]]] = Field(default=None, validation_alias=AliasChoices('contactPoint', 'https://schema.org/contactPoint'), serialization_alias='https://schema.org/contactPoint')
    affiliation: Optional[Union["Organization", List["Organization"]]] = Field(default=None, validation_alias=AliasChoices('affiliation', 'https://schema.org/affiliation'), serialization_alias='https://schema.org/affiliation')
    parent: Optional[Union["Person", List["Person"]]] = Field(default=None, validation_alias=AliasChoices('parent', 'https://schema.org/parent'), serialization_alias='https://schema.org/parent')
