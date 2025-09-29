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
from .store import Store

class OfficeEquipmentStore(Store):
    '''
    An office equipment store.
    '''
    class_: Literal['https://schema.org/OfficeEquipmentStore'] = Field( # type: ignore
        default='https://schema.org/OfficeEquipmentStore',
        alias='@type',
        serialization_alias='@type'
    )
