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
from .create_action import CreateAction

class FilmAction(CreateAction):
    '''
    The act of capturing sound and moving images on film, video, or digitally.
    '''
    class_: Literal['https://schema.org/FilmAction'] = Field( # type: ignore
        default='https://schema.org/FilmAction',
        alias='@type',
        serialization_alias='@type'
    )
