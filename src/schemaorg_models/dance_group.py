from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.performing_group import PerformingGroup


class DanceGroup(PerformingGroup):
    """
A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.
    """
    type_: Literal['https://schema.org/DanceGroup'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DanceGroup'),serialization_alias='class') # type: ignore
