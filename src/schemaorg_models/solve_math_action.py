from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.action import Action

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
