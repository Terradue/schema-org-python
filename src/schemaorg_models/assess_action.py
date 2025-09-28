from __future__ import annotations

from .action import Action    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AssessAction(Action):
    """
The act of forming one's opinion, reaction or sentiment.
    """
    class_: Literal['https://schema.org/AssessAction'] = Field( # type: ignore
        default='https://schema.org/AssessAction',
        alias='@type',
        serialization_alias='@type'
    )
