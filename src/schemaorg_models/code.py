from __future__ import annotations

from .creative_work import CreativeWork    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Code(CreativeWork):
    """
Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
    class_: Literal['https://schema.org/Code'] = Field( # type: ignore
        default='https://schema.org/Code',
        alias='@type',
        serialization_alias='@type'
    )
