from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.monetary_amount import MonetaryAmount

class DatedMoneySpecification(StructuredValue):
    """
A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.
    """
    class_: Literal['https://schema.org/DatedMoneySpecification'] = Field(default='https://schema.org/DatedMoneySpecification', alias='@type', serialization_alias='@type') # type: ignore
    currency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('currency', 'https://schema.org/currency'), serialization_alias='https://schema.org/currency')
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None, validation_alias=AliasChoices('endDate', 'https://schema.org/endDate'), serialization_alias='https://schema.org/endDate')
    amount: Optional[Union[MonetaryAmount, List[MonetaryAmount], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('amount', 'https://schema.org/amount'), serialization_alias='https://schema.org/amount')
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('startDate', 'https://schema.org/startDate'), serialization_alias='https://schema.org/startDate')
