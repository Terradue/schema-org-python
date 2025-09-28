from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.interact_action import InteractAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MarryAction(InteractAction):
    """
The act of marrying a person.
    """
    class_: Literal['https://schema.org/MarryAction'] = Field( # type: ignore
        default='https://schema.org/MarryAction',
        alias='@type',
        serialization_alias='@type'
    )
