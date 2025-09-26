from typing import Union, List, Optional
from datetime import date, datetime, time
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.day_of_week import DayOfWeek

class OpeningHoursSpecification(StructuredValue):
    """
The opening hours of a certain place.
    """
    dayOfWeek: Optional[Union[DayOfWeek, List[DayOfWeek]]] = Field(default=None,validation_alias=AliasChoices('dayOfWeek', 'https://schema.org/dayOfWeek'),serialization_alias='https://schema.org/dayOfWeek')
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'),serialization_alias='https://schema.org/validFrom')
    closes: Optional[Union[time, List[time]]] = Field(default=None,validation_alias=AliasChoices('closes', 'https://schema.org/closes'),serialization_alias='https://schema.org/closes')
    opens: Optional[Union[time, List[time]]] = Field(default=None,validation_alias=AliasChoices('opens', 'https://schema.org/opens'),serialization_alias='https://schema.org/opens')
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('validThrough', 'https://schema.org/validThrough'),serialization_alias='https://schema.org/validThrough')
