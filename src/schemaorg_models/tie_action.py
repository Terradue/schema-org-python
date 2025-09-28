from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.achieve_action import AchieveAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TieAction(AchieveAction):
    """
The act of reaching a draw in a competitive activity.
    """
    class_: Literal['https://schema.org/TieAction'] = Field( # type: ignore
        default='https://schema.org/TieAction',
        alias='@type',
        serialization_alias='@type'
    )
