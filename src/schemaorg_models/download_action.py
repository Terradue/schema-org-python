from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .transfer_action import TransferAction

class DownloadAction(TransferAction):
    '''
    The act of downloading an object.
    '''
    class_: Literal['https://schema.org/DownloadAction'] = Field( # type: ignore
        default='https://schema.org/DownloadAction',
        alias='@type',
        serialization_alias='@type'
    )
