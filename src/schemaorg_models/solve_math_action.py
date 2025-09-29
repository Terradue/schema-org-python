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
from .action import Action

class SolveMathAction(Action):
    '''
    The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.

    Attributes:
        eduQuestionType: For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open ended", "Flashcard".
    '''
    class_: Literal['https://schema.org/SolveMathAction'] = Field( # type: ignore
        default='https://schema.org/SolveMathAction',
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
