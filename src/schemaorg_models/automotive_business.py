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

class AutomotiveBusiness(LocalBusiness):
    '''
    Car repair, sales, or parts.
    '''
    class_: Literal['https://schema.org/AutomotiveBusiness'] = Field( # type: ignore
        default='https://schema.org/AutomotiveBusiness',
        alias='@type',
        serialization_alias='@type'
    )
