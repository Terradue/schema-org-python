from __future__ import annotations

from .react_action import ReactAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WantAction(ReactAction):
    """
The act of expressing a desire about the object. An agent wants an object.
    """
    class_: Literal['https://schema.org/WantAction'] = Field( # type: ignore
        default='https://schema.org/WantAction',
        alias='@type',
        serialization_alias='@type'
    )
