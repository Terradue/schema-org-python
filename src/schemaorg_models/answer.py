from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.comment import Comment

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.comment import Comment
from schemaorg_models.web_content import WebContent

class Answer(Comment):
    """
An answer offered to a question; perhaps correct, perhaps opinionated or wrong.
    """
    class_: Literal['https://schema.org/Answer'] = Field(default='https://schema.org/Answer', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    parentItem: Optional[Union[CreativeWork, List[CreativeWork], Comment, List[Comment]]] = Field(default=None, validation_alias=AliasChoices('parentItem', 'https://schema.org/parentItem'), serialization_alias='https://schema.org/parentItem')
    answerExplanation: Optional[Union[Comment, List[Comment], WebContent, List[WebContent]]] = Field(default=None, validation_alias=AliasChoices('answerExplanation', 'https://schema.org/answerExplanation'), serialization_alias='https://schema.org/answerExplanation')
