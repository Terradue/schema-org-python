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

class ClaimReview(Review):
    '''
    A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).

    Attributes:
        claimReviewed: A short summary of the specific claims reviewed in a ClaimReview.
    '''
    class_: Literal['https://schema.org/ClaimReview'] = Field( # type: ignore
        default='https://schema.org/ClaimReview',
        alias='@type',
        serialization_alias='@type'
    )
    claimReviewed: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
