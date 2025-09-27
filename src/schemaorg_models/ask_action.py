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
    type_: Literal['https://schema.org/AskAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AskAction'),serialization_alias='class') # type: ignore
    question: Optional[Union[Question, List[Question]]] = Field(default=None,validation_alias=AliasChoices('question', 'https://schema.org/question'),serialization_alias='https://schema.org/question')
