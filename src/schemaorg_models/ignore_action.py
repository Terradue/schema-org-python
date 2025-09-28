from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.assess_action import AssessAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class IgnoreAction(AssessAction):
    """
The act of intentionally disregarding the object. An agent ignores an object.
    """
    class_: Literal['https://schema.org/IgnoreAction'] = Field( # type: ignore
        default='https://schema.org/IgnoreAction',
        alias='@type',
        serialization_alias='@type'
    )
