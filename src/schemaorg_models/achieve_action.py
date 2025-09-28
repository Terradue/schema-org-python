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

class AchieveAction(Action):
    """
The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.
    """
    class_: Literal['https://schema.org/AchieveAction'] = Field( # type: ignore
        default='https://schema.org/AchieveAction',
        alias='@type',
        serialization_alias='@type'
    )
