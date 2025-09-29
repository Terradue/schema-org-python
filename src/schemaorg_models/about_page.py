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

class AboutPage(WebPage):
    '''
    Web page type: About page.
    '''
    class_: Literal['https://schema.org/AboutPage'] = Field( # type: ignore
        default='https://schema.org/AboutPage',
        alias='@type',
        serialization_alias='@type'
    )
