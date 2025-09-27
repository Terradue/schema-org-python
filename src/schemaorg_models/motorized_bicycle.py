from typing import Literal
from pydantic import Field
from schemaorg_models.vehicle import Vehicle


class MotorizedBicycle(Vehicle):
    """
A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.
    """
    class_: Literal['https://schema.org/MotorizedBicycle'] = Field('class', alias='class', serialization_alias='class') # type: ignore
