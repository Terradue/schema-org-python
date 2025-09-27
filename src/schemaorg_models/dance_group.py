from typing import Literal
from pydantic import Field
from schemaorg_models.performing_group import PerformingGroup


class DanceGroup(PerformingGroup):
    """
A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.
    """
    class_: Literal['https://schema.org/DanceGroup'] = Field(default='https://schema.org/DanceGroup', alias='@type', serialization_alias='@type') # type: ignore
