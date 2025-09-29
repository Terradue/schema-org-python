from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .performing_group import PerformingGroup

class DanceGroup(PerformingGroup):
    '''
    A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.
    '''
    class_: Literal['https://schema.org/DanceGroup'] = Field( # type: ignore
        default='https://schema.org/DanceGroup',
        alias='@type',
        serialization_alias='@type'
    )
