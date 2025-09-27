from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """
A motorcycle repair shop.
    """
    class_: Literal['https://schema.org/MotorcycleRepair'] = Field(default='https://schema.org/MotorcycleRepair', alias='class', serialization_alias='class') # type: ignore
