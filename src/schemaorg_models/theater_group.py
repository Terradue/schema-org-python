from typing import Literal
from pydantic import Field
from schemaorg_models.performing_group import PerformingGroup


class TheaterGroup(PerformingGroup):
    """
A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.
    """
    class_: Literal['https://schema.org/TheaterGroup'] = Field('class', alias='class', serialization_alias='class') # type: ignore
