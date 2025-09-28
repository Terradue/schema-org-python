from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .create_action import CreateAction

class PhotographAction(CreateAction):
    """
The act of capturing still images of objects using a camera.
    """
    class_: Literal['https://schema.org/PhotographAction'] = Field( # type: ignore
        default='https://schema.org/PhotographAction',
        alias='@type',
        serialization_alias='@type'
    )
