from __future__ import annotations

from .communicate_action import CommunicateAction    

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
from schemaorg_models.question import Question

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
