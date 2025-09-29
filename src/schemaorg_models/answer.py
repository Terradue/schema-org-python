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
from .comment import Comment
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .web_content import WebContent
    from .creative_work import CreativeWork

class Answer(Comment):
    '''
    An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    Attributes:
        parentItem: The parent of a question, answer or item in general. Typically used for Q/A discussion threads e.g. a chain of comments with the first comment being an [[Article]] or other [[CreativeWork]]. See also [[comment]] which points from something to a comment about it.
        answerExplanation: A step-by-step or full explanation about Answer. Can outline how this Answer was achieved or contain more broad clarification or statement about it. 
    '''
    class_: Literal['https://schema.org/Answer'] = Field( # type: ignore
        default='https://schema.org/Answer',
        alias='@type',
        serialization_alias='@type'
    )
    parentItem: Optional[Union['CreativeWork', List['CreativeWork'], 'Comment', List['Comment']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    answerExplanation: Optional[Union['Comment', List['Comment'], 'WebContent', List['WebContent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
