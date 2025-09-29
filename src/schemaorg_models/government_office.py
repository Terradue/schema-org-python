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

class GovernmentOffice(LocalBusiness):
    '''
    A government office&#x2014;for example, an IRS or DMV office.
    '''
    class_: Literal['https://schema.org/GovernmentOffice'] = Field( # type: ignore
        default='https://schema.org/GovernmentOffice',
        alias='@type',
        serialization_alias='@type'
    )
