from __future__ import annotations
from datetime import (
    date,
    datetime
)
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
    from .merchant_return_enumeration import MerchantReturnEnumeration
    from .monetary_amount import MonetaryAmount
    from .return_fees_enumeration import ReturnFeesEnumeration
    from .return_method_enumeration import ReturnMethodEnumeration
    from .refund_type_enumeration import RefundTypeEnumeration

class MerchantReturnPolicySeasonalOverride(Intangible):
    """
A seasonal override of a return policy, for example used for holidays.
    """
    class_: Literal['https://schema.org/MerchantReturnPolicySeasonalOverride'] = Field( # type: ignore
        default='https://schema.org/MerchantReturnPolicySeasonalOverride',
        alias='@type',
        serialization_alias='@type'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startDate',
            'https://schema.org/startDate'
        ),
        serialization_alias='https://schema.org/startDate'
    )
    returnFees: Optional[Union["ReturnFeesEnumeration", List["ReturnFeesEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnFees',
            'https://schema.org/returnFees'
        ),
        serialization_alias='https://schema.org/returnFees'
    )
    returnShippingFeesAmount: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnShippingFeesAmount',
            'https://schema.org/returnShippingFeesAmount'
        ),
        serialization_alias='https://schema.org/returnShippingFeesAmount'
    )
    returnPolicyCategory: Optional[Union["MerchantReturnEnumeration", List["MerchantReturnEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnPolicyCategory',
            'https://schema.org/returnPolicyCategory'
        ),
        serialization_alias='https://schema.org/returnPolicyCategory'
    )
    restockingFee: Optional[Union["MonetaryAmount", List["MonetaryAmount"], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'restockingFee',
            'https://schema.org/restockingFee'
        ),
        serialization_alias='https://schema.org/restockingFee'
    )
    merchantReturnDays: Optional[Union[date, List[date], int, List[int], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'merchantReturnDays',
            'https://schema.org/merchantReturnDays'
        ),
        serialization_alias='https://schema.org/merchantReturnDays'
    )
    refundType: Optional[Union["RefundTypeEnumeration", List["RefundTypeEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'refundType',
            'https://schema.org/refundType'
        ),
        serialization_alias='https://schema.org/refundType'
    )
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endDate',
            'https://schema.org/endDate'
        ),
        serialization_alias='https://schema.org/endDate'
    )
    returnMethod: Optional[Union["ReturnMethodEnumeration", List["ReturnMethodEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'returnMethod',
            'https://schema.org/returnMethod'
        ),
        serialization_alias='https://schema.org/returnMethod'
    )
