from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class PublicationIssue(CreativeWork):
    """
A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.\
\
See also [blog post](https://blog-schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    """
    class_: Literal['https://schema.org/PublicationIssue'] = Field(default='https://schema.org/PublicationIssue', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    pagination: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('pagination', 'https://schema.org/pagination'), serialization_alias='https://schema.org/pagination')
    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('pageStart', 'https://schema.org/pageStart'), serialization_alias='https://schema.org/pageStart')
    issueNumber: Optional[Union[str, List[str], int, List[int]]] = Field(default=None, validation_alias=AliasChoices('issueNumber', 'https://schema.org/issueNumber'), serialization_alias='https://schema.org/issueNumber')
    pageEnd: Optional[Union[str, List[str], int, List[int]]] = Field(default=None, validation_alias=AliasChoices('pageEnd', 'https://schema.org/pageEnd'), serialization_alias='https://schema.org/pageEnd')
