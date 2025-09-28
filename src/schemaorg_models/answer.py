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
from .comment import Comment
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .web_content import WebContent
    from .creative_work import CreativeWork

class Answer(Comment):
    """
An answer offered to a question; perhaps correct, perhaps opinionated or wrong.
    """
    class_: Literal['https://schema.org/Answer'] = Field( # type: ignore
        default='https://schema.org/Answer',
        alias='@type',
        serialization_alias='@type'
    )
    parentItem: Optional[Union["CreativeWork", List["CreativeWork"], "Comment", List["Comment"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentItem',
            'https://schema.org/parentItem'
        ),
        serialization_alias='https://schema.org/parentItem'
    )
    answerExplanation: Optional[Union["Comment", List["Comment"], "WebContent", List["WebContent"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'answerExplanation',
            'https://schema.org/answerExplanation'
        ),
        serialization_alias='https://schema.org/answerExplanation'
    )
