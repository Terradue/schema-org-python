from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.financial_product import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """
A service to convert funds from one currency to another currency.
    """
    type_: Literal['https://schema.org/CurrencyConversionService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CurrencyConversionService'),serialization_alias='class') # type: ignore
