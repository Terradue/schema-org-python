from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """
A motorcycle repair shop.
    """
    class_: Literal['https://schema.org/MotorcycleRepair'] = Field(default='https://schema.org/MotorcycleRepair', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
