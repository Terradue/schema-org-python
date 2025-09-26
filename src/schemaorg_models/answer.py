from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.comment import Comment

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.comment import Comment
from schemaorg_models.web_content import WebContent

class Answer(Comment):
    """
An answer offered to a question; perhaps correct, perhaps opinionated or wrong.
    """
    parentItem: Optional[Union[CreativeWork, List[CreativeWork], Comment, List[Comment]]] = Field(default=None,validation_alias=AliasChoices('parentItem', 'https://schema.org/parentItem'),serialization_alias='https://schema.org/parentItem')
    answerExplanation: Optional[Union[Comment, List[Comment], WebContent, List[WebContent]]] = Field(default=None,validation_alias=AliasChoices('answerExplanation', 'https://schema.org/answerExplanation'),serialization_alias='https://schema.org/answerExplanation')
