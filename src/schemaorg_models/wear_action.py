from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .use_action import UseAction

class WearAction(UseAction):
    """
The act of dressing oneself in clothing.
    """
    class_: Literal['https://schema.org/WearAction'] = Field( # type: ignore
        default='https://schema.org/WearAction',
        alias='@type',
        serialization_alias='@type'
    )
