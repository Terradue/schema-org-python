from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """
A motorcycle dealer.
    """
    type_: Literal['https://schema.org/MotorcycleDealer'] = Field(default='https://schema.org/MotorcycleDealer', alias='@type', serialization_alias='@type') # type: ignore
