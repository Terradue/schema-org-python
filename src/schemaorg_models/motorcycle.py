from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.vehicle import Vehicle


class Motorcycle(Vehicle):
    """
A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.
    """
    type_: Literal['https://schema.org/Motorcycle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Motorcycle'),serialization_alias='class') # type: ignore
