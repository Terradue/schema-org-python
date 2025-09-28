from __future__ import annotations

from .transfer_action import TransferAction    

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
