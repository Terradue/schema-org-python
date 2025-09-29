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
from .web_page_element import WebPageElement

class WPHeader(WebPageElement):
    '''
    The header section of the page.
    '''
    class_: Literal['https://schema.org/WPHeader'] = Field( # type: ignore
        default='https://schema.org/WPHeader',
        alias='@type',
        serialization_alias='@type'
    )
