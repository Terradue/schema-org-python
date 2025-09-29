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
from .financial_product import FinancialProduct
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .monetary_amount import MonetaryAmount

class PaymentCard(FinancialProduct):
    '''
    A payment method using a credit, debit, store or other card to associate the payment with an account.

    Attributes:
        monthlyMinimumRepaymentAmount: The minimum payment is the lowest amount of money that one is required to pay on a credit card statement each month.
        floorLimit: A floor limit is the amount of money above which credit card transactions must be authorized.
        cashBack: A cardholder benefit that pays the cardholder a small percentage of their net expenditures.
        contactlessPayment: A secure method for consumers to purchase products or services via debit, credit or smartcards by using RFID or NFC technology.
    '''
    class_: Literal['https://schema.org/PaymentCard'] = Field( # type: ignore
        default='https://schema.org/PaymentCard',
        alias='@type',
        serialization_alias='@type'
    )
    monthlyMinimumRepaymentAmount: Optional[Union[float, List[float], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    floorLimit: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    cashBack: Optional[Union[float, List[float], bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    contactlessPayment: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
