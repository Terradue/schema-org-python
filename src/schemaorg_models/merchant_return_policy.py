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
    from .member_program_tier import MemberProgramTier
    from .return_method_enumeration import ReturnMethodEnumeration
    from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .refund_type_enumeration import RefundTypeEnumeration
    from .return_label_source_enumeration import ReturnLabelSourceEnumeration
    from .property_value import PropertyValue
    from .offer_item_condition import OfferItemCondition
    from .country import Country
    from .monetary_amount import MonetaryAmount
    from .merchant_return_enumeration import MerchantReturnEnumeration
    from .return_fees_enumeration import ReturnFeesEnumeration

class MerchantReturnPolicy(Intangible):
    '''
    A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].

    Attributes:
        additionalProperty: A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\
\
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

        customerRemorseReturnShippingFeesAmount: The amount of shipping costs if a product is returned due to customer remorse. Applicable when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]].
        merchantReturnLink: Specifies a Web page or service by URL, for product returns.
        returnPolicyCountry: The country where the product has to be sent to for returns, for example "Ireland" using the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this can be different from the country where the product was originally shipped from or sent to.
        merchantReturnDays: Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].
        refundType: A refund type, from an enumerated list.
        returnMethod: The type of return method offered, specified from an enumeration.
        inStoreReturnsOffered: Are in-store returns offered? (For more advanced return methods use the [[returnMethod]] property.)
        itemDefectReturnFees: The type of return fees for returns of defect products.
        customerRemorseReturnFees: The type of return fees if the product is returned due to customer remorse.
        itemDefectReturnShippingFeesAmount: Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]] equals [[ReturnShippingFees]].
        returnFees: The type of return fees for purchased products (for any return reason).
        returnShippingFeesAmount: Amount of shipping costs for product returns (for any reason). Applicable when property [[returnFees]] equals [[ReturnShippingFees]].
        validForMemberTier: The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for.
        returnPolicyCategory: Specifies an applicable return policy (from an enumeration).
        customerRemorseReturnLabelSource: The method (from an enumeration) by which the customer obtains a return shipping label for a product returned due to customer remorse.
        returnPolicySeasonalOverride: Seasonal override of a return policy.
        itemDefectReturnLabelSource: The method (from an enumeration) by which the customer obtains a return shipping label for a defect product.
        applicableCountry: A country where a particular merchant return policy applies to, for example the two-letter ISO 3166-1 alpha-2 country code.
        returnLabelSource: The method (from an enumeration) by which the customer obtains a return shipping label for a product returned for any reason.
        restockingFee: Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use [[Number]] to specify a percentage of the product price paid by the customer.
        itemCondition: A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
    '''
    class_: Literal['https://schema.org/MerchantReturnPolicy'] = Field( # type: ignore
        default='https://schema.org/MerchantReturnPolicy',
        alias='@type',
        serialization_alias='@type'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    customerRemorseReturnShippingFeesAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
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
    returnPolicyCountry: Optional[Union[str, List[str], 'Country', List['Country']]] = Field(
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
    refundType: Optional[Union['RefundTypeEnumeration', List['RefundTypeEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'refundType',
            'https://schema.org/refundType'
        ),
        serialization_alias='https://schema.org/refundType'
    )
    returnMethod: Optional[Union['ReturnMethodEnumeration', List['ReturnMethodEnumeration']]] = Field(
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
    itemDefectReturnFees: Optional[Union['ReturnFeesEnumeration', List['ReturnFeesEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnFees',
            'https://schema.org/itemDefectReturnFees'
        ),
        serialization_alias='https://schema.org/itemDefectReturnFees'
    )
    customerRemorseReturnFees: Optional[Union['ReturnFeesEnumeration', List['ReturnFeesEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnFees',
            'https://schema.org/customerRemorseReturnFees'
        ),
        serialization_alias='https://schema.org/customerRemorseReturnFees'
    )
    itemDefectReturnShippingFeesAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnShippingFeesAmount',
            'https://schema.org/itemDefectReturnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/itemDefectReturnShippingFeesAmount'
    )
    returnFees: Optional[Union['ReturnFeesEnumeration', List['ReturnFeesEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnFees',
            'https://schema.org/returnFees'
        ),
        serialization_alias='https://schema.org/returnFees'
    )
    returnShippingFeesAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnShippingFeesAmount',
            'https://schema.org/returnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/returnShippingFeesAmount'
    )
    validForMemberTier: Optional[Union['MemberProgramTier', List['MemberProgramTier']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier',
            'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier'
    )
    returnPolicyCategory: Optional[Union['MerchantReturnEnumeration', List['MerchantReturnEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCategory',
            'https://schema.org/returnPolicyCategory'
        ),
        serialization_alias='https://schema.org/returnPolicyCategory'
    )
    customerRemorseReturnLabelSource: Optional[Union['ReturnLabelSourceEnumeration', List['ReturnLabelSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'customerRemorseReturnLabelSource',
            'https://schema.org/customerRemorseReturnLabelSource'
        ),
        serialization_alias='https://schema.org/customerRemorseReturnLabelSource'
    )
    returnPolicySeasonalOverride: Optional[Union['MerchantReturnPolicySeasonalOverride', List['MerchantReturnPolicySeasonalOverride']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicySeasonalOverride',
            'https://schema.org/returnPolicySeasonalOverride'
        ),
        serialization_alias='https://schema.org/returnPolicySeasonalOverride'
    )
    itemDefectReturnLabelSource: Optional[Union['ReturnLabelSourceEnumeration', List['ReturnLabelSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemDefectReturnLabelSource',
            'https://schema.org/itemDefectReturnLabelSource'
        ),
        serialization_alias='https://schema.org/itemDefectReturnLabelSource'
    )
    applicableCountry: Optional[Union['Country', List['Country'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'applicableCountry',
            'https://schema.org/applicableCountry'
        ),
        serialization_alias='https://schema.org/applicableCountry'
    )
    returnLabelSource: Optional[Union['ReturnLabelSourceEnumeration', List['ReturnLabelSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnLabelSource',
            'https://schema.org/returnLabelSource'
        ),
        serialization_alias='https://schema.org/returnLabelSource'
    )
    restockingFee: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'restockingFee',
            'https://schema.org/restockingFee'
        ),
        serialization_alias='https://schema.org/restockingFee'
    )
    itemCondition: Optional[Union['OfferItemCondition', List['OfferItemCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition',
            'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition'
    )
