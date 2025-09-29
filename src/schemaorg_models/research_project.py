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
from .project import Project

class ResearchProject(Project):
    '''
    A Research project.
    '''
    class_: Literal['https://schema.org/ResearchProject'] = Field( # type: ignore
        default='https://schema.org/ResearchProject',
        alias='@type',
        serialization_alias='@type'
    )
