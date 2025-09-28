from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.comment import Comment

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
