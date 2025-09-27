from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.performing_group import PerformingGroup


class TheaterGroup(PerformingGroup):
    """
A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.
    """
    type_: Literal['https://schema.org/TheaterGroup'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TheaterGroup'),serialization_alias='class') # type: ignore
