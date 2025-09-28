from __future__ import annotations

from .qualitative_value import QualitativeValue    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DriveWheelConfigurationValue(QualitativeValue):
    """
A value indicating which roadwheels will receive torque.
    """
    class_: Literal['https://schema.org/DriveWheelConfigurationValue'] = Field( # type: ignore
        default='https://schema.org/DriveWheelConfigurationValue',
        alias='@type',
        serialization_alias='@type'
    )
