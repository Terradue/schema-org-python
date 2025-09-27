from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction

from schemaorg_models.comment import Comment

class CommentAction(CommunicateAction):
    """
The act of generating a comment about a subject.
    """
    class_: Literal['https://schema.org/CommentAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    resultComment: Optional[Union[Comment, List[Comment]]] = Field(default=None,validation_alias=AliasChoices('resultComment', 'https://schema.org/resultComment'), serialization_alias='https://schema.org/resultComment')
