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
    from .answer import Answer
    from .creative_work import CreativeWork
    from .item_list import ItemList

class Question(Comment):
    '''
    A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.

    Attributes:
        eduQuestionType: For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open ended", "Flashcard".
        parentItem: The parent of a question, answer or item in general. Typically used for Q/A discussion threads e.g. a chain of comments with the first comment being an [[Article]] or other [[CreativeWork]]. See also [[comment]] which points from something to a comment about it.
        acceptedAnswer: The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.
        answerCount: The number of answers this question has received.
        suggestedAnswer: An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.
    '''
    class_: Literal['https://schema.org/Question'] = Field( # type: ignore
        default='https://schema.org/Question',
        alias='@type',
        serialization_alias='@type'
    )
    eduQuestionType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    parentItem: Optional[Union['CreativeWork', List['CreativeWork'], 'Comment', List['Comment']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    acceptedAnswer: Optional[Union['ItemList', List['ItemList'], 'Answer', List['Answer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    answerCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    suggestedAnswer: Optional[Union['Answer', List['Answer'], 'ItemList', List['ItemList']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
