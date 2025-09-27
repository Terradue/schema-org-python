from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.comment import Comment

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.comment import Comment
from schemaorg_models.item_list import ItemList

class Question(Comment):
    """
A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.
    """
    type_: Literal['https://schema.org/Question'] = Field(default='https://schema.org/Question', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    eduQuestionType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('eduQuestionType', 'https://schema.org/eduQuestionType'), serialization_alias='https://schema.org/eduQuestionType')
    parentItem: Optional[Union[CreativeWork, List[CreativeWork], Comment, List[Comment]]] = Field(default=None, validation_alias=AliasChoices('parentItem', 'https://schema.org/parentItem'), serialization_alias='https://schema.org/parentItem')
    acceptedAnswer: Optional[Union[ItemList, List[ItemList], "Answer", List["Answer"]]] = Field(default=None, validation_alias=AliasChoices('acceptedAnswer', 'https://schema.org/acceptedAnswer'), serialization_alias='https://schema.org/acceptedAnswer')
    answerCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('answerCount', 'https://schema.org/answerCount'), serialization_alias='https://schema.org/answerCount')
    suggestedAnswer: Optional[Union["Answer", List["Answer"], ItemList, List[ItemList]]] = Field(default=None, validation_alias=AliasChoices('suggestedAnswer', 'https://schema.org/suggestedAnswer'), serialization_alias='https://schema.org/suggestedAnswer')
