from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Chapter(CreativeWork):
    """
One of the sections into which a book is divided. A chapter usually has a section number or a name.
    """
    type_: Literal['https://schema.org/Chapter'] = Field(default='https://schema.org/Chapter', alias='@type', serialization_alias='@type') # type: ignore
    pageStart: Optional[Union[int, List[int], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('pageStart', 'https://schema.org/pageStart'), serialization_alias='https://schema.org/pageStart')
    pagination: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('pagination', 'https://schema.org/pagination'), serialization_alias='https://schema.org/pagination')
    pageEnd: Optional[Union[str, List[str], int, List[int]]] = Field(default=None, validation_alias=AliasChoices('pageEnd', 'https://schema.org/pageEnd'), serialization_alias='https://schema.org/pageEnd')
