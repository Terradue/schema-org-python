from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """
A motorcycle dealer.
    """
    class_: Literal['https://schema.org/MotorcycleDealer'] = Field('class', alias='class', serialization_alias='class') # type: ignore
