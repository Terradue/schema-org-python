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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .unit_price_specification import UnitPriceSpecification
    from .tier_benefit_enumeration import TierBenefitEnumeration
    from .monetary_amount import MonetaryAmount
    from .credit_card import CreditCard
    from .quantitative_value import QuantitativeValue
    from .member_program import MemberProgram

class MemberProgramTier(Intangible):
    '''
    A MemberProgramTier specifies a tier under a loyalty (member) program, for example "gold".

    Attributes:
        membershipPointsEarned: The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)
        hasTierBenefit: A member benefit for a particular tier of a loyalty program.
        isTierOf: The member program this tier is a part of.
        hasTierRequirement: A requirement for a user to join a membership tier, for example: a CreditCard if the tier requires sign up for a credit card, A UnitPriceSpecification if the user is required to pay a (periodic) fee, or a MonetaryAmount if the user needs to spend a minimum amount to join the tier. If a tier is free to join then this property does not need to be specified.
    '''
    class_: Literal['https://schema.org/MemberProgramTier'] = Field( # type: ignore
        default='https://schema.org/MemberProgramTier',
        alias='@type',
        serialization_alias='@type'
    )
    membershipPointsEarned: Optional[Union['QuantitativeValue', List['QuantitativeValue'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipPointsEarned',
            'https://schema.org/membershipPointsEarned'
        ),
        serialization_alias='https://schema.org/membershipPointsEarned'
    )
    hasTierBenefit: Optional[Union['TierBenefitEnumeration', List['TierBenefitEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTierBenefit',
            'https://schema.org/hasTierBenefit'
        ),
        serialization_alias='https://schema.org/hasTierBenefit'
    )
    isTierOf: Optional[Union['MemberProgram', List['MemberProgram']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isTierOf',
            'https://schema.org/isTierOf'
        ),
        serialization_alias='https://schema.org/isTierOf'
    )
    hasTierRequirement: Optional[Union['MonetaryAmount', List['MonetaryAmount'], 'CreditCard', List['CreditCard'], str, List[str], 'UnitPriceSpecification', List['UnitPriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTierRequirement',
            'https://schema.org/hasTierRequirement'
        ),
        serialization_alias='https://schema.org/hasTierRequirement'
    )
