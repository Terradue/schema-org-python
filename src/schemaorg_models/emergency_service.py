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

class EmergencyService(LocalBusiness):
    '''
    An emergency service, such as a fire station or ER.
    '''
    class_: Literal['https://schema.org/EmergencyService'] = Field( # type: ignore
        default='https://schema.org/EmergencyService',
        alias='@type',
        serialization_alias='@type'
    )
