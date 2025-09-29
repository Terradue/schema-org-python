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
from .review import Review

class EmployerReview(Review):
    '''
    An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer, written by a current or former employee of that organization.
    '''
    class_: Literal['https://schema.org/EmployerReview'] = Field( # type: ignore
        default='https://schema.org/EmployerReview',
        alias='@type',
        serialization_alias='@type'
    )
