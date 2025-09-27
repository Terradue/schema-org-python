from typing import List, Literal, Optional, Union
from datetime import time
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.day_of_week import DayOfWeek
from schemaorg_models.quantitative_value import QuantitativeValue

class ServicePeriod(StructuredValue):
    """
ServicePeriod represents a duration with some constraints about cutoff time and business days. This is used e.g. in shipping for handling times or transit time.
    """
    type_: Literal['https://schema.org/ServicePeriod'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ServicePeriod'),serialization_alias='class') # type: ignore
    businessDays: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"], DayOfWeek, List[DayOfWeek]]] = Field(default=None,validation_alias=AliasChoices('businessDays', 'https://schema.org/businessDays'),serialization_alias='https://schema.org/businessDays')
    duration: Optional[Union["Duration", List["Duration"], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('duration', 'https://schema.org/duration'),serialization_alias='https://schema.org/duration')
    cutoffTime: Optional[Union[time, List[time]]] = Field(default=None,validation_alias=AliasChoices('cutoffTime', 'https://schema.org/cutoffTime'),serialization_alias='https://schema.org/cutoffTime')
