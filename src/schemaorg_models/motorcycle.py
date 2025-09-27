from typing import Literal
from pydantic import Field
from schemaorg_models.vehicle import Vehicle


class Motorcycle(Vehicle):
    """
A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.
    """
    class_: Literal['https://schema.org/Motorcycle'] = Field('class', alias='class', serialization_alias='class') # type: ignore
