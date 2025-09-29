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
from .organization import Organization

class WorkersUnion(Organization):
    '''
    A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization that promotes the interests of its worker members by collectively bargaining with management, organizing, and political lobbying.
    '''
    class_: Literal['https://schema.org/WorkersUnion'] = Field( # type: ignore
        default='https://schema.org/WorkersUnion',
        alias='@type',
        serialization_alias='@type'
    )
