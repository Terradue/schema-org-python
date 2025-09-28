from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .action import Action

class FindAction(Action):
    """
The act of finding an object.\
\
Related actions:\
\
* [[SearchAction]]: FindAction is generally lead by a SearchAction, but not necessarily.
    """
    class_: Literal['https://schema.org/FindAction'] = Field( # type: ignore
        default='https://schema.org/FindAction',
        alias='@type',
        serialization_alias='@type'
    )
