from __future__ import annotations

from .review import Review    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class ClaimReview(Review):
    """
A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).
    """
    class_: Literal['https://schema.org/ClaimReview'] = Field( # type: ignore
        default='https://schema.org/ClaimReview',
        alias='@type',
        serialization_alias='@type'
    )
    claimReviewed: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'claimReviewed',
            'https://schema.org/claimReviewed'
        ),
        serialization_alias='https://schema.org/claimReviewed'
    )
