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

class QAPage(WebPage):
    '''
    A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs).
    '''
    class_: Literal['https://schema.org/QAPage'] = Field( # type: ignore
        default='https://schema.org/QAPage',
        alias='@type',
        serialization_alias='@type'
    )
