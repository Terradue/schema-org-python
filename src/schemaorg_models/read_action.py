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

class ReadAction(ConsumeAction):
    """
The act of consuming written content.
    """
    class_: Literal['https://schema.org/ReadAction'] = Field( # type: ignore
        default='https://schema.org/ReadAction',
        alias='@type',
        serialization_alias='@type'
    )
