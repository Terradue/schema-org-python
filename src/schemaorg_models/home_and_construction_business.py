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

class HomeAndConstructionBusiness(LocalBusiness):
    '''
    A construction business.\
\
A HomeAndConstructionBusiness is a [[LocalBusiness]] that provides services around homes and buildings.\
\
As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\\(s).
    '''
    class_: Literal['https://schema.org/HomeAndConstructionBusiness'] = Field( # type: ignore
        default='https://schema.org/HomeAndConstructionBusiness',
        alias='@type',
        serialization_alias='@type'
    )
