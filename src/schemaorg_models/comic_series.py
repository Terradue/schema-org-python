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
from .periodical import Periodical

class ComicSeries(Periodical):
    '''
    A sequential publication of comic stories under a
    	unifying title, for example "The Amazing Spider-Man" or "Groo the
    	Wanderer".
    '''
    class_: Literal['https://schema.org/ComicSeries'] = Field( # type: ignore
        default='https://schema.org/ComicSeries',
        alias='@type',
        serialization_alias='@type'
    )
