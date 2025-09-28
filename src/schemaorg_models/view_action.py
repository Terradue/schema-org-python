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

class ViewAction(ConsumeAction):
    """
The act of consuming static visual content.
    """
    class_: Literal['https://schema.org/ViewAction'] = Field( # type: ignore
        default='https://schema.org/ViewAction',
        alias='@type',
        serialization_alias='@type'
    )
