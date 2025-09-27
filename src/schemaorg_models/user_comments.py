from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.user_interaction import UserInteraction

from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.creative_work import CreativeWork

class UserComments(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserComments'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    commentTime: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('commentTime', 'https://schema.org/commentTime'), serialization_alias='https://schema.org/commentTime')
    replyToUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('replyToUrl', 'https://schema.org/replyToUrl'), serialization_alias='https://schema.org/replyToUrl')
    @field_serializer('replyToUrl')
    def replyToUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    creator: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('creator', 'https://schema.org/creator'), serialization_alias='https://schema.org/creator')
    discusses: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('discusses', 'https://schema.org/discusses'), serialization_alias='https://schema.org/discusses')
    commentText: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('commentText', 'https://schema.org/commentText'), serialization_alias='https://schema.org/commentText')
