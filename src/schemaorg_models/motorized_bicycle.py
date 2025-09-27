from typing import Literal
from pydantic import Field
from schemaorg_models.vehicle import Vehicle


class MotorizedBicycle(Vehicle):
    """
A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to assist with pedaling.
    """
    type_: Literal['https://schema.org/MotorizedBicycle'] = Field(default='https://schema.org/MotorizedBicycle', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
