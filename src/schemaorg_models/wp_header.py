from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page_element import WebPageElement

class WPHeader(WebPageElement):
    """
The header section of the page.
    """
    class_: Literal['https://schema.org/WPHeader'] = Field( # type: ignore
        default='https://schema.org/WPHeader',
        alias='@type',
        serialization_alias='@type'
    )
