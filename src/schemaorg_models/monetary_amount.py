from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.structured_value import StructuredValue

class MonetaryAmount(StructuredValue):
    """
A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc.
    """
    type_: Literal['https://schema.org/MonetaryAmount'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MonetaryAmount'),serialization_alias='class') # type: ignore
    currency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('currency', 'https://schema.org/currency'),serialization_alias='https://schema.org/currency')
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('validThrough', 'https://schema.org/validThrough'),serialization_alias='https://schema.org/validThrough')
    minValue: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('minValue', 'https://schema.org/minValue'),serialization_alias='https://schema.org/minValue')
    value: Optional[Union[float, List[float], StructuredValue, List[StructuredValue], bool, List[bool], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('value', 'https://schema.org/value'),serialization_alias='https://schema.org/value')
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),serialization_alias='https://schema.org/validFrom')
    maxValue: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('maxValue', 'https://schema.org/maxValue'),serialization_alias='https://schema.org/maxValue')
