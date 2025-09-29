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
from .organization import Organization

class OnlineBusiness(Organization):
    '''
    A particular online business, either standalone or the online part of a broader organization. Examples include an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping provider, an online (virtual) doctor, etc.
    '''
    class_: Literal['https://schema.org/OnlineBusiness'] = Field( # type: ignore
        default='https://schema.org/OnlineBusiness',
        alias='@type',
        serialization_alias='@type'
    )
