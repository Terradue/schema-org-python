from __future__ import annotations

from .comment import Comment    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CorrectionComment(Comment):
    """
A [[comment]] that corrects [[CreativeWork]].
    """
    class_: Literal['https://schema.org/CorrectionComment'] = Field( # type: ignore
        default='https://schema.org/CorrectionComment',
        alias='@type',
        serialization_alias='@type'
    )
