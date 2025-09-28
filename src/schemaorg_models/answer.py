from __future__ import annotations

from .comment import Comment    

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
from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.web_content import WebContent

class Answer(Comment):
    """
An answer offered to a question; perhaps correct, perhaps opinionated or wrong.
    """
    class_: Literal['https://schema.org/Answer'] = Field( # type: ignore
        default='https://schema.org/Answer',
        alias='@type',
        serialization_alias='@type'
    )
    parentItem: Optional[Union[CreativeWork, List[CreativeWork], Comment, List[Comment]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'parentItem',
            'https://schema.org/parentItem'
        ),
        serialization_alias='https://schema.org/parentItem'
    )
    answerExplanation: Optional[Union[Comment, List[Comment], WebContent, List[WebContent]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'answerExplanation',
            'https://schema.org/answerExplanation'
        ),
        serialization_alias='https://schema.org/answerExplanation'
    )
