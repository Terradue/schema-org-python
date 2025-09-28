from __future__ import annotations

from .how_to_item import HowToItem    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HowToTool(HowToItem):
    """
A tool used (but not consumed) when performing instructions for how to achieve a result.
    """
    class_: Literal['https://schema.org/HowToTool'] = Field( # type: ignore
        default='https://schema.org/HowToTool',
        alias='@type',
        serialization_alias='@type'
    )
