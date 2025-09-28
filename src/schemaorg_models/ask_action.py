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
from .communicate_action import CommunicateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .question import Question

class AskAction(CommunicateAction):
    """
The act of posing a question / favor to someone.\
\
Related actions:\
\
* [[ReplyAction]]: Appears generally as a response to AskAction.
    """
    class_: Literal['https://schema.org/AskAction'] = Field( # type: ignore
        default='https://schema.org/AskAction',
        alias='@type',
        serialization_alias='@type'
    )
    question: Optional[Union[Question, List[Question]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'question',
            'https://schema.org/question'
        ),
        serialization_alias='https://schema.org/question'
    )
