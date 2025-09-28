from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page_element import WebPageElement

class WPSideBar(WebPageElement):
    """
A sidebar section of the page.
    """
    class_: Literal['https://schema.org/WPSideBar'] = Field( # type: ignore
        default='https://schema.org/WPSideBar',
        alias='@type',
        serialization_alias='@type'
    )
