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
from .local_business import LocalBusiness

class TouristInformationCenter(LocalBusiness):
    '''
    A tourist information center.
    '''
    class_: Literal['https://schema.org/TouristInformationCenter'] = Field( # type: ignore
        default='https://schema.org/TouristInformationCenter',
        alias='@type',
        serialization_alias='@type'
    )
