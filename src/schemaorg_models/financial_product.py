from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.service import Service


class FinancialProduct(Service):
    """
A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.
    """
    class_: Literal['https://schema.org/FinancialProduct'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    interestRate: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('interestRate', 'https://schema.org/interestRate'), serialization_alias='https://schema.org/interestRate')
    annualPercentageRate: Optional[Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('annualPercentageRate', 'https://schema.org/annualPercentageRate'), serialization_alias='https://schema.org/annualPercentageRate')
    feesAndCommissionsSpecification: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('feesAndCommissionsSpecification', 'https://schema.org/feesAndCommissionsSpecification'), serialization_alias='https://schema.org/feesAndCommissionsSpecification')
    @field_serializer('feesAndCommissionsSpecification')
    def feesAndCommissionsSpecification2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

