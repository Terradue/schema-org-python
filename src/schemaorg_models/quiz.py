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
from .learning_resource import LearningResource

class Quiz(LearningResource):
    '''
    Quiz: A test of knowledge, skills and abilities.
    '''
    class_: Literal['https://schema.org/Quiz'] = Field( # type: ignore
        default='https://schema.org/Quiz',
        alias='@type',
        serialization_alias='@type'
    )
