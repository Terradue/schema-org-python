from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """
A gas station.
    """
    class_: Literal['https://schema.org/GasStation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
