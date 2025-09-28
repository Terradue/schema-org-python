from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.use_action import UseAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WearAction(UseAction):
    """
The act of dressing oneself in clothing.
    """
    class_: Literal['https://schema.org/WearAction'] = Field( # type: ignore
        default='https://schema.org/WearAction',
        alias='@type',
        serialization_alias='@type'
    )
