from __future__ import annotations
from datetime import (
    time
)
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue
    from .day_of_week import DayOfWeek

class ServicePeriod(StructuredValue):
    """
ServicePeriod represents a duration with some constraints about cutoff time and business days. This is used e.g. in shipping for handling times or transit time.
    """
    class_: Literal['https://schema.org/ServicePeriod'] = Field( # type: ignore
        default='https://schema.org/ServicePeriod',
        alias='@type',
        serialization_alias='@type'
    )
    businessDays: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"], "DayOfWeek", List["DayOfWeek"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessDays',
            'https://schema.org/businessDays'
        ),
        serialization_alias='https://schema.org/businessDays'
    )
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    cutoffTime: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cutoffTime',
            'https://schema.org/cutoffTime'
        ),
        serialization_alias='https://schema.org/cutoffTime'
    )
