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
from .lodging_business import LodgingBusiness

class VacationRental(LodgingBusiness):
    '''
    A kind of lodging business that focuses on renting single properties for limited time.
    '''
    class_: Literal['https://schema.org/VacationRental'] = Field( # type: ignore
        default='https://schema.org/VacationRental',
        alias='@type',
        serialization_alias='@type'
    )
