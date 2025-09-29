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
from .how_to_item import HowToItem

class HowToTool(HowToItem):
    '''
    A tool used (but not consumed) when performing instructions for how to achieve a result.
    '''
    class_: Literal['https://schema.org/HowToTool'] = Field( # type: ignore
        default='https://schema.org/HowToTool',
        alias='@type',
        serialization_alias='@type'
    )
