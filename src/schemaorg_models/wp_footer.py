from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page_element import WebPageElement

class WPFooter(WebPageElement):
    """
The footer section of the page.
    """
    class_: Literal['https://schema.org/WPFooter'] = Field( # type: ignore
        default='https://schema.org/WPFooter',
        alias='@type',
        serialization_alias='@type'
    )
