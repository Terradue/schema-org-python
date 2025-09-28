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

class OrganizeAction(Action):
    """
The act of manipulating/administering/supervising/controlling one or more objects.
    """
    class_: Literal['https://schema.org/OrganizeAction'] = Field( # type: ignore
        default='https://schema.org/OrganizeAction',
        alias='@type',
        serialization_alias='@type'
    )
