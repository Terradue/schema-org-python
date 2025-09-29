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
from .action import Action

class CreateAction(Action):
    '''
    The act of deliberately creating/producing/generating/building a result out of the agent.
    '''
    class_: Literal['https://schema.org/CreateAction'] = Field( # type: ignore
        default='https://schema.org/CreateAction',
        alias='@type',
        serialization_alias='@type'
    )
