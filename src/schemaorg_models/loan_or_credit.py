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
    from .thing import Thing
    from .repayment_specification import RepaymentSpecification
    from .quantitative_value import QuantitativeValue
    from .duration import Duration

class LoanOrCredit(FinancialProduct):
    '''
    A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.

    Attributes:
        gracePeriod: The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred.
        requiredCollateral: Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)
        currency: The currency in which the monetary amount is expressed.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        loanRepaymentForm: A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment.
        amount: The amount of money.
        recourseLoan: The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money.
        loanTerm: The duration of the loan or credit agreement.
        loanType: The type of a loan or credit.
        renegotiableLoan: Whether the terms for payment of interest can be renegotiated during the life of the loan.
    '''
    class_: Literal['https://schema.org/LoanOrCredit'] = Field( # type: ignore
        default='https://schema.org/LoanOrCredit',
        alias='@type',
        serialization_alias='@type'
    )
    gracePeriod: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    requiredCollateral: Optional[Union[str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    currency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    loanRepaymentForm: Optional[Union['RepaymentSpecification', List['RepaymentSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    amount: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    recourseLoan: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    loanTerm: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    loanType: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    renegotiableLoan: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
