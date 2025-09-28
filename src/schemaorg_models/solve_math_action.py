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
from .action import Action

class SolveMathAction(Action):
    """
The action that takes in a math expression and directs users to a page potentially capable of solving/simplifying that expression.
    """
    class_: Literal['https://schema.org/SolveMathAction'] = Field( # type: ignore
        default='https://schema.org/SolveMathAction',
        alias='@type',
        serialization_alias='@type'
    )
    eduQuestionType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eduQuestionType',
            'https://schema.org/eduQuestionType'
        ),
        serialization_alias='https://schema.org/eduQuestionType'
    )
