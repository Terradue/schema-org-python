from __future__ import annotations

from .update_action import UpdateAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DeleteAction(UpdateAction):
    """
The act of editing a recipient by removing one of its objects.
    """
    class_: Literal['https://schema.org/DeleteAction'] = Field( # type: ignore
        default='https://schema.org/DeleteAction',
        alias='@type',
        serialization_alias='@type'
    )
