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

class UserReview(Review):
    '''
    A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast with [[CriticReview]].
    '''
    class_: Literal['https://schema.org/UserReview'] = Field( # type: ignore
        default='https://schema.org/UserReview',
        alias='@type',
        serialization_alias='@type'
    )
