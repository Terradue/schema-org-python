from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.member_program_tier import MemberProgramTier
from schemaorg_models.merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride

class MerchantReturnPolicy(Intangible):
    """
A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].
    """
    type_: Literal['https://schema.org/MerchantReturnPolicy'] = Field(default='https://schema.org/MerchantReturnPolicy', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(default=None, validation_alias=AliasChoices('additionalProperty', 'https://schema.org/additionalProperty'), serialization_alias='https://schema.org/additionalProperty')
    customerRemorseReturnShippingFeesAmount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('customerRemorseReturnShippingFeesAmount', 'https://schema.org/customerRemorseReturnShippingFeesAmount'), serialization_alias='https://schema.org/customerRemorseReturnShippingFeesAmount')
    merchantReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('merchantReturnLink', 'https://schema.org/merchantReturnLink'), serialization_alias='https://schema.org/merchantReturnLink')
    @field_serializer('merchantReturnLink')
    def merchantReturnLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    returnPolicyCountry: Optional[Union[str, List[str], "Country", List["Country"]]] = Field(default=None, validation_alias=AliasChoices('returnPolicyCountry', 'https://schema.org/returnPolicyCountry'), serialization_alias='https://schema.org/returnPolicyCountry')
    merchantReturnDays: Optional[Union[date, List[date], int, List[int], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('merchantReturnDays', 'https://schema.org/merchantReturnDays'), serialization_alias='https://schema.org/merchantReturnDays')
    refundType: Optional[Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('refundType', 'https://schema.org/refundType'), serialization_alias='https://schema.org/refundType')
    returnMethod: Optional[Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('returnMethod', 'https://schema.org/returnMethod'), serialization_alias='https://schema.org/returnMethod')
    inStoreReturnsOffered: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('inStoreReturnsOffered', 'https://schema.org/inStoreReturnsOffered'), serialization_alias='https://schema.org/inStoreReturnsOffered')
    itemDefectReturnFees: Optional[Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('itemDefectReturnFees', 'https://schema.org/itemDefectReturnFees'), serialization_alias='https://schema.org/itemDefectReturnFees')
    customerRemorseReturnFees: Optional[Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('customerRemorseReturnFees', 'https://schema.org/customerRemorseReturnFees'), serialization_alias='https://schema.org/customerRemorseReturnFees')
    itemDefectReturnShippingFeesAmount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('itemDefectReturnShippingFeesAmount', 'https://schema.org/itemDefectReturnShippingFeesAmount'), serialization_alias='https://schema.org/itemDefectReturnShippingFeesAmount')
    returnFees: Optional[Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('returnFees', 'https://schema.org/returnFees'), serialization_alias='https://schema.org/returnFees')
    returnShippingFeesAmount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(default=None, validation_alias=AliasChoices('returnShippingFeesAmount', 'https://schema.org/returnShippingFeesAmount'), serialization_alias='https://schema.org/returnShippingFeesAmount')
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(default=None, validation_alias=AliasChoices('validForMemberTier', 'https://schema.org/validForMemberTier'), serialization_alias='https://schema.org/validForMemberTier')
    returnPolicyCategory: Optional[Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('returnPolicyCategory', 'https://schema.org/returnPolicyCategory'), serialization_alias='https://schema.org/returnPolicyCategory')
    customerRemorseReturnLabelSource: Optional[Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('customerRemorseReturnLabelSource', 'https://schema.org/customerRemorseReturnLabelSource'), serialization_alias='https://schema.org/customerRemorseReturnLabelSource')
    returnPolicySeasonalOverride: Optional[Union[MerchantReturnPolicySeasonalOverride, List[MerchantReturnPolicySeasonalOverride]]] = Field(default=None, validation_alias=AliasChoices('returnPolicySeasonalOverride', 'https://schema.org/returnPolicySeasonalOverride'), serialization_alias='https://schema.org/returnPolicySeasonalOverride')
    itemDefectReturnLabelSource: Optional[Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('itemDefectReturnLabelSource', 'https://schema.org/itemDefectReturnLabelSource'), serialization_alias='https://schema.org/itemDefectReturnLabelSource')
    applicableCountry: Optional[Union["Country", List["Country"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('applicableCountry', 'https://schema.org/applicableCountry'), serialization_alias='https://schema.org/applicableCountry')
    returnLabelSource: Optional[Union["ReturnLabelSourceEnumeration", List["ReturnLabelSourceEnumeration"]]] = Field(default=None, validation_alias=AliasChoices('returnLabelSource', 'https://schema.org/returnLabelSource'), serialization_alias='https://schema.org/returnLabelSource')
    restockingFee: Optional[Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('restockingFee', 'https://schema.org/restockingFee'), serialization_alias='https://schema.org/restockingFee')
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = Field(default=None, validation_alias=AliasChoices('itemCondition', 'https://schema.org/itemCondition'), serialization_alias='https://schema.org/itemCondition')
