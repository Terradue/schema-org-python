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
from .web_page import WebPage

class SearchResultsPage(WebPage):
    '''
    Web page type: Search results page.
    '''
    class_: Literal['https://schema.org/SearchResultsPage'] = Field( # type: ignore
        default='https://schema.org/SearchResultsPage',
        alias='@type',
        serialization_alias='@type'
    )
