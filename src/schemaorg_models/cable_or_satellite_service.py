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

class CableOrSatelliteService(Service):
    '''
    A service which provides access to media programming like TV or radio. Access may be via cable or satellite.
    '''
    class_: Literal['https://schema.org/CableOrSatelliteService'] = Field( # type: ignore
        default='https://schema.org/CableOrSatelliteService',
        alias='@type',
        serialization_alias='@type'
    )
