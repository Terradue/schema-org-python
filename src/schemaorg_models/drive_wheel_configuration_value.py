from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.qualitative_value import QualitativeValue


class DriveWheelConfigurationValue(QualitativeValue):
    """
A value indicating which roadwheels will receive torque.
    """
    type_: Literal['https://schema.org/DriveWheelConfigurationValue'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DriveWheelConfigurationValue'),serialization_alias='class') # type: ignore
