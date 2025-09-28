from __future__ import annotations

from .allocate_action import AllocateAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AcceptAction(AllocateAction):
    """
The act of committing to/adopting an object.\
\
Related actions:\
\
* [[RejectAction]]: The antonym of AcceptAction.
    """
    class_: Literal['https://schema.org/AcceptAction'] = Field( # type: ignore
        default='https://schema.org/AcceptAction',
        alias='@type',
        serialization_alias='@type'
    )
