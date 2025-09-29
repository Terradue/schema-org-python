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
    from .return_fees_enumeration import ReturnFeesEnumeration
    from .monetary_amount import MonetaryAmount
    from .return_method_enumeration import ReturnMethodEnumeration
    from .merchant_return_enumeration import MerchantReturnEnumeration

class MerchantReturnPolicySeasonalOverride(Intangible):
    '''
    A seasonal override of a return policy, for example used for holidays.

    Attributes:
        startDate: The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        returnFees: The type of return fees for purchased products (for any return reason).
        returnShippingFeesAmount: Amount of shipping costs for product returns (for any reason). Applicable when property [[returnFees]] equals [[ReturnShippingFees]].
        returnPolicyCategory: Specifies an applicable return policy (from an enumeration).
        restockingFee: Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use [[Number]] to specify a percentage of the product price paid by the customer.
        merchantReturnDays: Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].
        refundType: A refund type, from an enumerated list.
        endDate: The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        returnMethod: The type of return method offered, specified from an enumeration.
    '''
    class_: Literal['https://schema.org/MerchantReturnPolicySeasonalOverride'] = Field( # type: ignore
        default='https://schema.org/MerchantReturnPolicySeasonalOverride',
        alias='@type',
        serialization_alias='@type'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
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
    returnPolicyCategory: Optional[Union['MerchantReturnEnumeration', List['MerchantReturnEnumeration']]] = Field(
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
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
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
