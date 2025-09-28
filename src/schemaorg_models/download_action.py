from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.transfer_action import TransferAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DownloadAction(TransferAction):
    """
The act of downloading an object.
    """
    class_: Literal['https://schema.org/DownloadAction'] = Field( # type: ignore
        default='https://schema.org/DownloadAction',
        alias='@type',
        serialization_alias='@type'
    )
