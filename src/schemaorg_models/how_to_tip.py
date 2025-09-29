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
from .creative_work import CreativeWork

class HowToTip(CreativeWork):
    '''
    An explanation in the instructions for how to achieve a result. It provides supplementary information about a technique, supply, author's preference, etc. It can explain what could be done, or what should not be done, but doesn't specify what should be done (see HowToDirection).
    '''
    class_: Literal['https://schema.org/HowToTip'] = Field( # type: ignore
        default='https://schema.org/HowToTip',
        alias='@type',
        serialization_alias='@type'
    )
