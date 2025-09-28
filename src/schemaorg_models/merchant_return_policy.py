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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .merchant_return_enumeration import MerchantReturnEnumeration
    from .return_method_enumeration import ReturnMethodEnumeration
    from .offer_item_condition import OfferItemCondition
    from .member_program_tier import MemberProgramTier
    from .return_fees_enumeration import ReturnFeesEnumeration
    from .return_label_source_enumeration import ReturnLabelSourceEnumeration
    from .refund_type_enumeration import RefundTypeEnumeration
    from .monetary_amount import MonetaryAmount
    from .country import Country
    from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .property_value import PropertyValue

class MerchantReturnPolicy(Intangible):
    """
A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].
    """
    class_: Literal['https://schema.org/MerchantReturnPolicy'] = Field( # type: ignore
        default='https://schema.org/MerchantReturnPolicy',
        alias='@type',
        serialization_alias='@type'
    )
    additionalProperty: Optional[Union[PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    customerRemorseReturnShippingFeesAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnShippingFeesAmount',
            'https://schema.org/customerRemorseReturnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/customerRemorseReturnShippingFeesAmount'
    )
    merchantReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchantReturnLink',
            'https://schema.org/merchantReturnLink'
        ),
        serialization_alias='https://schema.org/merchantReturnLink'
    )
    returnPolicyCountry: Optional[Union[str, List[str], Country, List[Country]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCountry',
            'https://schema.org/returnPolicyCountry'
        ),
        serialization_alias='https://schema.org/returnPolicyCountry'
    )
    merchantReturnDays: Optional[Union[date, List[date], int, List[int], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchantReturnDays',
            'https://schema.org/merchantReturnDays'
        ),
        serialization_alias='https://schema.org/merchantReturnDays'
    )
    refundType: Optional[Union[RefundTypeEnumeration, List[RefundTypeEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'refundType',
            'https://schema.org/refundType'
        ),
        serialization_alias='https://schema.org/refundType'
    )
    returnMethod: Optional[Union[ReturnMethodEnumeration, List[ReturnMethodEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnMethod',
            'https://schema.org/returnMethod'
        ),
        serialization_alias='https://schema.org/returnMethod'
    )
    inStoreReturnsOffered: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inStoreReturnsOffered',
            'https://schema.org/inStoreReturnsOffered'
        ),
        serialization_alias='https://schema.org/inStoreReturnsOffered'
    )
    itemDefectReturnFees: Optional[Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnFees',
            'https://schema.org/itemDefectReturnFees'
        ),
        serialization_alias='https://schema.org/itemDefectReturnFees'
    )
    customerRemorseReturnFees: Optional[Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnFees',
            'https://schema.org/customerRemorseReturnFees'
        ),
        serialization_alias='https://schema.org/customerRemorseReturnFees'
    )
    itemDefectReturnShippingFeesAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnShippingFeesAmount',
            'https://schema.org/itemDefectReturnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/itemDefectReturnShippingFeesAmount'
    )
    returnFees: Optional[Union[ReturnFeesEnumeration, List[ReturnFeesEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnFees',
            'https://schema.org/returnFees'
        ),
        serialization_alias='https://schema.org/returnFees'
    )
    returnShippingFeesAmount: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnShippingFeesAmount',
            'https://schema.org/returnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/returnShippingFeesAmount'
    )
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier',
            'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier'
    )
    returnPolicyCategory: Optional[Union[MerchantReturnEnumeration, List[MerchantReturnEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCategory',
            'https://schema.org/returnPolicyCategory'
        ),
        serialization_alias='https://schema.org/returnPolicyCategory'
    )
    customerRemorseReturnLabelSource: Optional[Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnLabelSource',
            'https://schema.org/customerRemorseReturnLabelSource'
        ),
        serialization_alias='https://schema.org/customerRemorseReturnLabelSource'
    )
    returnPolicySeasonalOverride: Optional[Union[MerchantReturnPolicySeasonalOverride, List[MerchantReturnPolicySeasonalOverride]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicySeasonalOverride',
            'https://schema.org/returnPolicySeasonalOverride'
        ),
        serialization_alias='https://schema.org/returnPolicySeasonalOverride'
    )
    itemDefectReturnLabelSource: Optional[Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnLabelSource',
            'https://schema.org/itemDefectReturnLabelSource'
        ),
        serialization_alias='https://schema.org/itemDefectReturnLabelSource'
    )
    applicableCountry: Optional[Union[Country, List[Country], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicableCountry',
            'https://schema.org/applicableCountry'
        ),
        serialization_alias='https://schema.org/applicableCountry'
    )
    returnLabelSource: Optional[Union[ReturnLabelSourceEnumeration, List[ReturnLabelSourceEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnLabelSource',
            'https://schema.org/returnLabelSource'
        ),
        serialization_alias='https://schema.org/returnLabelSource'
    )
    restockingFee: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'restockingFee',
            'https://schema.org/restockingFee'
        ),
        serialization_alias='https://schema.org/restockingFee'
    )
    itemCondition: Optional[Union[OfferItemCondition, List[OfferItemCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition',
            'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition'
    )
