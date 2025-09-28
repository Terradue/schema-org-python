from __future__ import annotations

from .item_list import ItemList    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HowToStep(ItemList):
    """
A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.
    """
    class_: Literal['https://schema.org/HowToStep'] = Field( # type: ignore
        default='https://schema.org/HowToStep',
        alias='@type',
        serialization_alias='@type'
    )
