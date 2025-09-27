from typing import Literal
from pydantic import Field
from schemaorg_models.financial_product import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """
A service to convert funds from one currency to another currency.
    """
    class_: Literal['https://schema.org/CurrencyConversionService'] = Field('class', alias='class', serialization_alias='class') # type: ignore
