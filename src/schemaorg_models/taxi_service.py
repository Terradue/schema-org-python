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
from .service import Service

class TaxiService(Service):
    '''
    A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.
    '''
    class_: Literal['https://schema.org/TaxiService'] = Field( # type: ignore
        default='https://schema.org/TaxiService',
        alias='@type',
        serialization_alias='@type'
    )
