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
    from .refund_type_enumeration import RefundTypeEnumeration
    from .monetary_amount import MonetaryAmount
    from .return_fees_enumeration import ReturnFeesEnumeration
    from .member_program_tier import MemberProgramTier
    from .return_method_enumeration import ReturnMethodEnumeration
    from .offer_item_condition import OfferItemCondition
    from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .return_label_source_enumeration import ReturnLabelSourceEnumeration
    from .property_value import PropertyValue
    from .merchant_return_enumeration import MerchantReturnEnumeration
    from .country import Country

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    customerRemorseReturnShippingFeesAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    merchantReturnLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnPolicyCountry: Optional[Union[str, List[str], 'Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    merchantReturnDays: Optional[Union[date, List[date], int, List[int], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    refundType: Optional[Union['RefundTypeEnumeration', List['RefundTypeEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnMethod: Optional[Union['ReturnMethodEnumeration', List['ReturnMethodEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    inStoreReturnsOffered: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itemDefectReturnFees: Optional[Union['ReturnFeesEnumeration', List['ReturnFeesEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    customerRemorseReturnFees: Optional[Union['ReturnFeesEnumeration', List['ReturnFeesEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itemDefectReturnShippingFeesAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnFees: Optional[Union['ReturnFeesEnumeration', List['ReturnFeesEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnShippingFeesAmount: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validForMemberTier: Optional[Union['MemberProgramTier', List['MemberProgramTier']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnPolicyCategory: Optional[Union['MerchantReturnEnumeration', List['MerchantReturnEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    customerRemorseReturnLabelSource: Optional[Union['ReturnLabelSourceEnumeration', List['ReturnLabelSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnPolicySeasonalOverride: Optional[Union['MerchantReturnPolicySeasonalOverride', List['MerchantReturnPolicySeasonalOverride']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itemDefectReturnLabelSource: Optional[Union['ReturnLabelSourceEnumeration', List['ReturnLabelSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    applicableCountry: Optional[Union['Country', List['Country'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    returnLabelSource: Optional[Union['ReturnLabelSourceEnumeration', List['ReturnLabelSourceEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    restockingFee: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itemCondition: Optional[Union['OfferItemCondition', List['OfferItemCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
