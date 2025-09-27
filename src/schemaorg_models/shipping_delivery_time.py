from typing import List, Literal, Optional, Union
from datetime import time
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.day_of_week import DayOfWeek
from schemaorg_models.service_period import ServicePeriod
from schemaorg_models.quantitative_value import QuantitativeValue

class ShippingDeliveryTime(StructuredValue):
    """
ShippingDeliveryTime provides various pieces of information about delivery times for shipping.
    """
    class_: Literal['https://schema.org/ShippingDeliveryTime'] = Field(default='https://schema.org/ShippingDeliveryTime', alias='@type', serialization_alias='@type') # type: ignore
    businessDays: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"], DayOfWeek, List[DayOfWeek]]] = Field(default=None, validation_alias=AliasChoices('businessDays', 'https://schema.org/businessDays'), serialization_alias='https://schema.org/businessDays')
    transitTime: Optional[Union[ServicePeriod, List[ServicePeriod], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('transitTime', 'https://schema.org/transitTime'), serialization_alias='https://schema.org/transitTime')
    handlingTime: Optional[Union[ServicePeriod, List[ServicePeriod], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None, validation_alias=AliasChoices('handlingTime', 'https://schema.org/handlingTime'), serialization_alias='https://schema.org/handlingTime')
    cutoffTime: Optional[Union[time, List[time]]] = Field(default=None, validation_alias=AliasChoices('cutoffTime', 'https://schema.org/cutoffTime'), serialization_alias='https://schema.org/cutoffTime')
