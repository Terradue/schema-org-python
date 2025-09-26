from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class MemberProgramTier(Intangible):
    """
A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold".
    """
    membershipPointsEarned: Optional[Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('membershipPointsEarned', 'https://schema.org/membershipPointsEarned'),serialization_alias='https://schema.org/membershipPointsEarned')
    hasTierBenefit: Optional[Union["TierBenefitEnumeration", List["TierBenefitEnumeration"]]] = Field(default=None,validation_alias=AliasChoices('hasTierBenefit', 'https://schema.org/hasTierBenefit'),serialization_alias='https://schema.org/hasTierBenefit')
    isTierOf: Optional[Union["MemberProgram", List["MemberProgram"]]] = Field(default=None,validation_alias=AliasChoices('isTierOf', 'https://schema.org/isTierOf'),serialization_alias='https://schema.org/isTierOf')
    hasTierRequirement: Optional[Union["MonetaryAmount", List["MonetaryAmount"], "CreditCard", List["CreditCard"], str, List[str], "UnitPriceSpecification", List["UnitPriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('hasTierRequirement', 'https://schema.org/hasTierRequirement'),serialization_alias='https://schema.org/hasTierRequirement')
