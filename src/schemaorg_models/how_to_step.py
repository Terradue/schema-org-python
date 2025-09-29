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
from .item_list import ItemList

class HowToStep(ItemList):
    '''
    A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.
    '''
    class_: Literal['https://schema.org/HowToStep'] = Field( # type: ignore
        default='https://schema.org/HowToStep',
        alias='@type',
        serialization_alias='@type'
    )
