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
from .communicate_action import CommunicateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .question import Question

class AskAction(CommunicateAction):
    '''
    The act of posing a question / favor to someone.\
\
Related actions:\
\
* [[ReplyAction]]: Appears generally as a response to AskAction.

    Attributes:
        question: A sub property of object. A question.
    '''
    class_: Literal['https://schema.org/AskAction'] = Field( # type: ignore
        default='https://schema.org/AskAction',
        alias='@type',
        serialization_alias='@type'
    )
    question: Optional[Union['Question', List['Question']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'question',
            'https://schema.org/question'
        ),
        serialization_alias='https://schema.org/question'
    )
