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
    from .comment import Comment

class CommentAction(CommunicateAction):
    '''
    The act of generating a comment about a subject.

    Attributes:
        resultComment: A sub property of result. The Comment created or sent as a result of this action.
    '''
    class_: Literal['https://schema.org/CommentAction'] = Field( # type: ignore
        default='https://schema.org/CommentAction',
        alias='@type',
        serialization_alias='@type'
    )
    resultComment: Optional[Union['Comment', List['Comment']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'resultComment',
            'https://schema.org/resultComment'
        ),
        serialization_alias='https://schema.org/resultComment'
    )
