from __future__ import annotations
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
from .review import Review
from .assess_action import AssessAction

class ReviewAction(AssessAction):
    """
The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.
    """
    class_: Literal['https://schema.org/ReviewAction'] = Field( # type: ignore
        default='https://schema.org/ReviewAction',
        alias='@type',
        serialization_alias='@type'
    )
    resultReview: Optional[Union[Review, List[Review]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'resultReview',
            'https://schema.org/resultReview'
        ),
        serialization_alias='https://schema.org/resultReview'
    )
