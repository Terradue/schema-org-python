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

class InteractAction(Action):
    """
The act of interacting with another person or organization.
    """
    class_: Literal['https://schema.org/InteractAction'] = Field( # type: ignore
        default='https://schema.org/InteractAction',
        alias='@type',
        serialization_alias='@type'
    )
