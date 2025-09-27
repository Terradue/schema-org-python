from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.comment import Comment

class ReplyAction(CommunicateAction):
    """
The act of responding to a question/message asked/sent by the object. Related to [[AskAction]].\
\
Related actions:\
\
* [[AskAction]]: Appears generally as an origin of a ReplyAction.
    """
    class_: Literal['https://schema.org/ReplyAction'] = Field(default='https://schema.org/ReplyAction', alias='@type', serialization_alias='@type') # type: ignore
    resultComment: Optional[Union[Comment, List[Comment]]] = Field(default=None, validation_alias=AliasChoices('resultComment', 'https://schema.org/resultComment'), serialization_alias='https://schema.org/resultComment')
