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
from .government_building import GovernmentBuilding

class DefenceEstablishment(GovernmentBuilding):
    '''
    A defence establishment, such as an army or navy base.
    '''
    class_: Literal['https://schema.org/DefenceEstablishment'] = Field( # type: ignore
        default='https://schema.org/DefenceEstablishment',
        alias='@type',
        serialization_alias='@type'
    )
