from __future__ import annotations

from .insert_action import InsertAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AppendAction(InsertAction):
    """
The act of inserting at the end if an ordered collection.
    """
    class_: Literal['https://schema.org/AppendAction'] = Field( # type: ignore
        default='https://schema.org/AppendAction',
        alias='@type',
        serialization_alias='@type'
    )
