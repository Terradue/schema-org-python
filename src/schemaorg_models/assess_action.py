from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.action import Action

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AssessAction(Action):
    """
The act of forming one's opinion, reaction or sentiment.
    """
    class_: Literal['https://schema.org/AssessAction'] = Field( # type: ignore
        default='https://schema.org/AssessAction',
        alias='@type',
        serialization_alias='@type'
    )
