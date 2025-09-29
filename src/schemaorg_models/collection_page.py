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

class CollectionPage(WebPage):
    '''
    Web page type: Collection page.
    '''
    class_: Literal['https://schema.org/CollectionPage'] = Field( # type: ignore
        default='https://schema.org/CollectionPage',
        alias='@type',
        serialization_alias='@type'
    )
