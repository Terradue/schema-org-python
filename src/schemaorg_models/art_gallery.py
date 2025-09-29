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
from .entertainment_business import EntertainmentBusiness

class ArtGallery(EntertainmentBusiness):
    '''
    An art gallery.
    '''
    class_: Literal['https://schema.org/ArtGallery'] = Field( # type: ignore
        default='https://schema.org/ArtGallery',
        alias='@type',
        serialization_alias='@type'
    )
