from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class Courthouse(GovernmentBuilding):
    """
A courthouse.
    """
    class_: Literal['https://schema.org/Courthouse'] = Field('class', alias='class', serialization_alias='class') # type: ignore
