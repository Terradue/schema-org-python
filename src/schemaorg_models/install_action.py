from __future__ import annotations

from .consume_action import ConsumeAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class InstallAction(ConsumeAction):
    """
The act of installing an application.
    """
    class_: Literal['https://schema.org/InstallAction'] = Field( # type: ignore
        default='https://schema.org/InstallAction',
        alias='@type',
        serialization_alias='@type'
    )
