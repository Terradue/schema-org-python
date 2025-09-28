from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.qualitative_value import QualitativeValue

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
