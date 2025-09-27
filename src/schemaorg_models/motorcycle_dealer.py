from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """
A motorcycle dealer.
    """
    class_: Literal['https://schema.org/MotorcycleDealer'] = Field(default='https://schema.org/MotorcycleDealer', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
