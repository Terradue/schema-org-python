from __future__ import annotations
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
from .service import Service
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class FinancialProduct(Service):
    """
A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.
    """
    class_: Literal['https://schema.org/FinancialProduct'] = Field( # type: ignore
        default='https://schema.org/FinancialProduct',
        alias='@type',
        serialization_alias='@type'
    )
    interestRate: Optional[Union[float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interestRate',
            'https://schema.org/interestRate'
        ),
        serialization_alias='https://schema.org/interestRate'
    )
    annualPercentageRate: Optional[Union[QuantitativeValue, List[QuantitativeValue], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'annualPercentageRate',
            'https://schema.org/annualPercentageRate'
        ),
        serialization_alias='https://schema.org/annualPercentageRate'
    )
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'feesAndCommissionsSpecification',
            'https://schema.org/feesAndCommissionsSpecification'
        ),
        serialization_alias='https://schema.org/feesAndCommissionsSpecification'
    )
