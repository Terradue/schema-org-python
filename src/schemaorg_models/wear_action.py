from __future__ import annotations

from .use_action import UseAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WearAction(UseAction):
    """
The act of dressing oneself in clothing.
    """
    class_: Literal['https://schema.org/WearAction'] = Field( # type: ignore
        default='https://schema.org/WearAction',
        alias='@type',
        serialization_alias='@type'
    )
