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

class FAQPage(WebPage):
    '''
    A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]]).
    '''
    class_: Literal['https://schema.org/FAQPage'] = Field( # type: ignore
        default='https://schema.org/FAQPage',
        alias='@type',
        serialization_alias='@type'
    )
