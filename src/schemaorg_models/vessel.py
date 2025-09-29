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
from .anatomical_structure import AnatomicalStructure

class Vessel(AnatomicalStructure):
    '''
    A component of the human body circulatory system comprised of an intricate network of hollow tubes that transport blood throughout the entire body.
    '''
    class_: Literal['https://schema.org/Vessel'] = Field( # type: ignore
        default='https://schema.org/Vessel',
        alias='@type',
        serialization_alias='@type'
    )
