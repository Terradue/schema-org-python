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
    from .comment import Comment

class ReplyAction(CommunicateAction):
    """
The act of responding to a question/message asked/sent by the object. Related to [[AskAction]].\
\
Related actions:\
\
* [[AskAction]]: Appears generally as an origin of a ReplyAction.
    """
    class_: Literal['https://schema.org/ReplyAction'] = Field( # type: ignore
        default='https://schema.org/ReplyAction',
        alias='@type',
        serialization_alias='@type'
    )
    resultComment: Optional[Union[Comment, List[Comment]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'resultComment',
            'https://schema.org/resultComment'
        ),
        serialization_alias='https://schema.org/resultComment'
    )
