from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """
A gas station.
    """
    type_: Literal['https://schema.org/GasStation'] = Field(default='https://schema.org/GasStation', alias='@type', serialization_alias='@type') # type: ignore
