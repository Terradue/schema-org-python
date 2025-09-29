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

class SearchAction(Action):
    '''
    The act of searching for an object.\
\
Related actions:\
\
* [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily.

    Attributes:
        query: A sub property of instrument. The query used on this action.
    '''
    class_: Literal['https://schema.org/SearchAction'] = Field( # type: ignore
        default='https://schema.org/SearchAction',
        alias='@type',
        serialization_alias='@type'
    )
    query: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
