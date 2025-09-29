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

class Table(WebPageElement):
    '''
    A table on a Web page.
    '''
    class_: Literal['https://schema.org/Table'] = Field( # type: ignore
        default='https://schema.org/Table',
        alias='@type',
        serialization_alias='@type'
    )
