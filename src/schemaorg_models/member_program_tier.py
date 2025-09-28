from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount
    from .credit_card import CreditCard
    from .member_program import MemberProgram
    from .quantitative_value import QuantitativeValue
    from .tier_benefit_enumeration import TierBenefitEnumeration
    from .unit_price_specification import UnitPriceSpecification

class MemberProgramTier(Intangible):
    """
A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold".
    """
    class_: Literal['https://schema.org/MemberProgramTier'] = Field( # type: ignore
        default='https://schema.org/MemberProgramTier',
        alias='@type',
        serialization_alias='@type'
    )
    membershipPointsEarned: Optional[Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipPointsEarned',
            'https://schema.org/membershipPointsEarned'
        ),
        serialization_alias='https://schema.org/membershipPointsEarned'
    )
    hasTierBenefit: Optional[Union["TierBenefitEnumeration", List["TierBenefitEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTierBenefit',
            'https://schema.org/hasTierBenefit'
        ),
        serialization_alias='https://schema.org/hasTierBenefit'
    )
    isTierOf: Optional[Union["MemberProgram", List["MemberProgram"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isTierOf',
            'https://schema.org/isTierOf'
        ),
        serialization_alias='https://schema.org/isTierOf'
    )
    hasTierRequirement: Optional[Union["MonetaryAmount", List["MonetaryAmount"], "CreditCard", List["CreditCard"], str, List[str], "UnitPriceSpecification", List["UnitPriceSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTierRequirement',
            'https://schema.org/hasTierRequirement'
        ),
        serialization_alias='https://schema.org/hasTierRequirement'
    )
