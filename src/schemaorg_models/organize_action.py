from __future__ import annotations

from .action import Action    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OrganizeAction(Action):
    """
The act of manipulating/administering/supervising/controlling one or more objects.
    """
    class_: Literal['https://schema.org/OrganizeAction'] = Field( # type: ignore
        default='https://schema.org/OrganizeAction',
        alias='@type',
        serialization_alias='@type'
    )
