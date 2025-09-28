from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.consume_action import ConsumeAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EatAction(ConsumeAction):
    """
The act of swallowing solid objects.
    """
    class_: Literal['https://schema.org/EatAction'] = Field( # type: ignore
        default='https://schema.org/EatAction',
        alias='@type',
        serialization_alias='@type'
    )
