from typing import Literal
from pydantic import Field
from schemaorg_models.qualitative_value import QualitativeValue


class DriveWheelConfigurationValue(QualitativeValue):
    """
A value indicating which roadwheels will receive torque.
    """
    class_: Literal['https://schema.org/DriveWheelConfigurationValue'] = Field(default='https://schema.org/DriveWheelConfigurationValue', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
