from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.service import Service


class FinancialProduct(Service):
    """
A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.
    """
    interestRate: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('interestRate', 'https://schema.org/interestRate'),serialization_alias='https://schema.org/interestRate')
    annualPercentageRate: Optional[Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('annualPercentageRate', 'https://schema.org/annualPercentageRate'),serialization_alias='https://schema.org/annualPercentageRate')
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('feesAndCommissionsSpecification', 'https://schema.org/feesAndCommissionsSpecification'),serialization_alias='https://schema.org/feesAndCommissionsSpecification')
