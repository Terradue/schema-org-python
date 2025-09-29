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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .speakable_specification import SpeakableSpecification

class Article(CreativeWork):
    '''
    An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.\
\
See also [blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).

    Attributes:
        pagination: Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        articleBody: The actual body of the article.
        pageEnd: The page on which the work ends; for example "138" or "xvi".
        backstory: For an [[Article]], typically a [[NewsArticle]], the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.
        wordCount: The number of words in the text of the CreativeWork such as an Article, Book, etc.
        articleSection: Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.
        speakable: Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.

The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:

1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.

2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.

3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.


For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For this
we define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.
         
        pageStart: The page on which the work starts; for example "135" or "xiii".
    '''
    class_: Literal['https://schema.org/Article'] = Field( # type: ignore
        default='https://schema.org/Article',
        alias='@type',
        serialization_alias='@type'
    )
    pagination: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pagination',
            'https://schema.org/pagination'
        ),
        serialization_alias='https://schema.org/pagination'
    )
    articleBody: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'articleBody',
            'https://schema.org/articleBody'
        ),
        serialization_alias='https://schema.org/articleBody'
    )
    pageEnd: Optional[Union[str, List[str], int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pageEnd',
            'https://schema.org/pageEnd'
        ),
        serialization_alias='https://schema.org/pageEnd'
    )
    backstory: Optional[Union[str, List[str], 'CreativeWork', List['CreativeWork']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'backstory',
            'https://schema.org/backstory'
        ),
        serialization_alias='https://schema.org/backstory'
    )
    wordCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'wordCount',
            'https://schema.org/wordCount'
        ),
        serialization_alias='https://schema.org/wordCount'
    )
    articleSection: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'articleSection',
            'https://schema.org/articleSection'
        ),
        serialization_alias='https://schema.org/articleSection'
    )
    speakable: Optional[Union[HttpUrl, List[HttpUrl], 'SpeakableSpecification', List['SpeakableSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'speakable',
            'https://schema.org/speakable'
        ),
        serialization_alias='https://schema.org/speakable'
    )
    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pageStart',
            'https://schema.org/pageStart'
        ),
        serialization_alias='https://schema.org/pageStart'
    )
