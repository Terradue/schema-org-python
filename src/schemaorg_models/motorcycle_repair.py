from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """
A motorcycle repair shop.
    """
    type_: Literal['https://schema.org/MotorcycleRepair'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MotorcycleRepair'),serialization_alias='class') # type: ignore
