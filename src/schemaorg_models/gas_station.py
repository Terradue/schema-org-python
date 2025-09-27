from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """
A gas station.
    """
    type_: Literal['https://schema.org/GasStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GasStation'),serialization_alias='class') # type: ignore
