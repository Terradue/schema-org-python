from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """
A motorcycle dealer.
    """
    type_: Literal['https://schema.org/MotorcycleDealer'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MotorcycleDealer'),serialization_alias='class') # type: ignore
