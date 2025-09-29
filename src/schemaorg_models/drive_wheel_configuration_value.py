from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .qualitative_value import QualitativeValue

class DriveWheelConfigurationValue(QualitativeValue):
    '''
    A value indicating which roadwheels will receive torque.
    '''
    class_: Literal['https://schema.org/DriveWheelConfigurationValue'] = Field( # type: ignore
        default='https://schema.org/DriveWheelConfigurationValue',
        alias='@type',
        serialization_alias='@type'
    )
