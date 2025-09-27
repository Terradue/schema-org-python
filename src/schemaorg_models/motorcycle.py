from typing import Literal
from pydantic import Field
from schemaorg_models.vehicle import Vehicle


class Motorcycle(Vehicle):
    """
A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.
    """
    class_: Literal['https://schema.org/Motorcycle'] = Field(default='https://schema.org/Motorcycle', alias='@type', serialization_alias='@type') # type: ignore
