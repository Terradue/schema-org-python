from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.speakable_specification import SpeakableSpecification

class Article(CreativeWork):
    """
An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.\
\
See also [blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """
    type_: Literal['https://schema.org/Article'] = Field(default='https://schema.org/Article', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    pagination: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('pagination', 'https://schema.org/pagination'), serialization_alias='https://schema.org/pagination')
    articleBody: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('articleBody', 'https://schema.org/articleBody'), serialization_alias='https://schema.org/articleBody')
    pageEnd: Optional[Union[str, List[str], int, List[int]]] = Field(default=None, validation_alias=AliasChoices('pageEnd', 'https://schema.org/pageEnd'), serialization_alias='https://schema.org/pageEnd')
    backstory: Optional[Union[str, List[str], CreativeWork, List[CreativeWork]]] = Field(default=None, validation_alias=AliasChoices('backstory', 'https://schema.org/backstory'), serialization_alias='https://schema.org/backstory')
    wordCount: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('wordCount', 'https://schema.org/wordCount'), serialization_alias='https://schema.org/wordCount')
    articleSection: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('articleSection', 'https://schema.org/articleSection'), serialization_alias='https://schema.org/articleSection')
    speakable: Optional[Union[HttpUrl, List[HttpUrl], SpeakableSpecification, List[SpeakableSpecification]]] = Field(default=None, validation_alias=AliasChoices('speakable', 'https://schema.org/speakable'), serialization_alias='https://schema.org/speakable')
    @field_serializer('speakable')
    def speakable2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('pageStart', 'https://schema.org/pageStart'), serialization_alias='https://schema.org/pageStart')
