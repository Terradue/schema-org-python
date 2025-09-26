from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.monetary_amount import MonetaryAmount

class ExchangeRateSpecification(StructuredValue):
    """
A structured value representing exchange rate.
    """
    exchangeRateSpread: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('exchangeRateSpread', 'https://schema.org/exchangeRateSpread'),serialization_alias='https://schema.org/exchangeRateSpread')
    currency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('currency', 'https://schema.org/currency'),serialization_alias='https://schema.org/currency')
    currentExchangeRate: Optional[Union["UnitPriceSpecification", List["UnitPriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('currentExchangeRate', 'https://schema.org/currentExchangeRate'),serialization_alias='https://schema.org/currentExchangeRate')
