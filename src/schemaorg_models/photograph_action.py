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

class PhotographAction(CreateAction):
    '''
    The act of capturing still images of objects using a camera.
    '''
    class_: Literal['https://schema.org/PhotographAction'] = Field( # type: ignore
        default='https://schema.org/PhotographAction',
        alias='@type',
        serialization_alias='@type'
    )
