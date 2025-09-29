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
from .assess_action import AssessAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .review import Review

class ReviewAction(AssessAction):
    '''
    The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

    Attributes:
        resultReview: A sub property of result. The review that resulted in the performing of the action.
    '''
    class_: Literal['https://schema.org/ReviewAction'] = Field( # type: ignore
        default='https://schema.org/ReviewAction',
        alias='@type',
        serialization_alias='@type'
    )
    resultReview: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'resultReview',
            'https://schema.org/resultReview'
        ),
        serialization_alias='https://schema.org/resultReview'
    )
