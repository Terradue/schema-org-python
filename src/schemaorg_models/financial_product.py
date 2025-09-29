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
from .service import Service
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue

class FinancialProduct(Service):
    '''
    A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.

    Attributes:
        interestRate: The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.
        annualPercentageRate: The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.
        feesAndCommissionsSpecification: Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    '''
    class_: Literal['https://schema.org/FinancialProduct'] = Field( # type: ignore
        default='https://schema.org/FinancialProduct',
        alias='@type',
        serialization_alias='@type'
    )
    interestRate: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'interestRate',
            'https://schema.org/interestRate'
        ),
        serialization_alias='https://schema.org/interestRate'
    )
    annualPercentageRate: Optional[Union['QuantitativeValue', List['QuantitativeValue'], float, List[float]]] = Field(
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
