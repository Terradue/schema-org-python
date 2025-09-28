from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .consume_action import ConsumeAction

class InstallAction(ConsumeAction):
    """
The act of installing an application.
    """
    class_: Literal['https://schema.org/InstallAction'] = Field( # type: ignore
        default='https://schema.org/InstallAction',
        alias='@type',
        serialization_alias='@type'
    )
