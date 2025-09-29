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

class EmploymentAgency(LocalBusiness):
    '''
    An employment agency.
    '''
    class_: Literal['https://schema.org/EmploymentAgency'] = Field( # type: ignore
        default='https://schema.org/EmploymentAgency',
        alias='@type',
        serialization_alias='@type'
    )
