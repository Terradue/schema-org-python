from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.article import Article


class NewsArticle(Article):
    """
A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.

A more detailed overview of [schema.org News markup](/docs/news.html) is also available.

    """
    class_: Literal['https://schema.org/NewsArticle'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    printColumn: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('printColumn', 'https://schema.org/printColumn'), serialization_alias='https://schema.org/printColumn')
    dateline: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('dateline', 'https://schema.org/dateline'), serialization_alias='https://schema.org/dateline')
    printEdition: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('printEdition', 'https://schema.org/printEdition'), serialization_alias='https://schema.org/printEdition')
    printSection: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('printSection', 'https://schema.org/printSection'), serialization_alias='https://schema.org/printSection')
    printPage: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('printPage', 'https://schema.org/printPage'), serialization_alias='https://schema.org/printPage')
