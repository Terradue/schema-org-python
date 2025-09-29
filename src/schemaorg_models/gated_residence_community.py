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
from .residence import Residence

class GatedResidenceCommunity(Residence):
    '''
    Residence type: Gated community.
    '''
    class_: Literal['https://schema.org/GatedResidenceCommunity'] = Field( # type: ignore
        default='https://schema.org/GatedResidenceCommunity',
        alias='@type',
        serialization_alias='@type'
    )
