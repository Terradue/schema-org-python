from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.find_action import FindAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DiscoverAction(FindAction):
    """
The act of discovering/finding an object.
    """
    class_: Literal['https://schema.org/DiscoverAction'] = Field( # type: ignore
        default='https://schema.org/DiscoverAction',
        alias='@type',
        serialization_alias='@type'
    )
