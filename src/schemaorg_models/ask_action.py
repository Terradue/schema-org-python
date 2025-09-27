from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.question import Question

class AskAction(CommunicateAction):
    """
The act of posing a question / favor to someone.\
\
Related actions:\
\
* [[ReplyAction]]: Appears generally as a response to AskAction.
    """
    class_: Literal['https://schema.org/AskAction'] = Field(default='https://schema.org/AskAction', alias='@type', serialization_alias='@type') # type: ignore
    question: Optional[Union[Question, List[Question]]] = Field(default=None, validation_alias=AliasChoices('question', 'https://schema.org/question'), serialization_alias='https://schema.org/question')
