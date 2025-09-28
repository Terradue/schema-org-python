from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page import WebPage

class ContactPage(WebPage):
    """
Web page type: Contact page.
    """
    class_: Literal['https://schema.org/ContactPage'] = Field( # type: ignore
        default='https://schema.org/ContactPage',
        alias='@type',
        serialization_alias='@type'
    )
