from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page import WebPage

class FAQPage(WebPage):
    """
A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]]).
    """
    class_: Literal['https://schema.org/FAQPage'] = Field( # type: ignore
        default='https://schema.org/FAQPage',
        alias='@type',
        serialization_alias='@type'
    )
