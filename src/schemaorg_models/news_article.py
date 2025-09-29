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
from .article import Article

class NewsArticle(Article):
    '''
    A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.

A more detailed overview of [schema.org News markup](/docs/news.html) is also available.


    Attributes:
        printColumn: The number of the column in which the NewsArticle appears in the print edition.
        dateline: A [dateline](https://en.wikipedia.org/wiki/Dateline) is a brief piece of text included in news articles that describes where and when the story was written or filed though the date is often omitted. Sometimes only a placename is provided.

Structured representations of dateline-related information can also be expressed more explicitly using [[locationCreated]] (which represents where a work was created, e.g. where a news report was written).  For location depicted or described in the content, use [[contentLocation]].

Dateline summaries are oriented more towards human readers than towards automated processing, and can vary substantially. Some examples: "BEIRUT, Lebanon, June 2.", "Paris, France", "December 19, 2017 11:43AM Reporting from Washington", "Beijing/Moscow", "QUEZON CITY, Philippines".
      
        printEdition: The edition of the print product in which the NewsArticle appears.
        printSection: If this NewsArticle appears in print, this field indicates the print section in which the article appeared.
        printPage: If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).
    '''
    class_: Literal['https://schema.org/NewsArticle'] = Field( # type: ignore
        default='https://schema.org/NewsArticle',
        alias='@type',
        serialization_alias='@type'
    )
    printColumn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    dateline: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    printEdition: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    printSection: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    printPage: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
