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

class InvestmentOrDeposit(FinancialProduct):
    '''
    A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.

    Attributes:
        amount: The amount of money.
    '''
    class_: Literal['https://schema.org/InvestmentOrDeposit'] = Field( # type: ignore
        default='https://schema.org/InvestmentOrDeposit',
        alias='@type',
        serialization_alias='@type'
    )
    amount: Optional[Union['MonetaryAmount', List['MonetaryAmount'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
