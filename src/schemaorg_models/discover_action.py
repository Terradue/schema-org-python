from __future__ import annotations

from .find_action import FindAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DiscoverAction(FindAction):
    """
The act of discovering/finding an object.
    """
    class_: Literal['https://schema.org/DiscoverAction'] = Field( # type: ignore
        default='https://schema.org/DiscoverAction',
        alias='@type',
        serialization_alias='@type'
    )
