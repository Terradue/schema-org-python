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

class WatchAction(ConsumeAction):
    """
The act of consuming dynamic/moving visual content.
    """
    class_: Literal['https://schema.org/WatchAction'] = Field( # type: ignore
        default='https://schema.org/WatchAction',
        alias='@type',
        serialization_alias='@type'
    )
