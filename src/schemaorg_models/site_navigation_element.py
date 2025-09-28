from __future__ import annotations

from .web_page_element import WebPageElement    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SiteNavigationElement(WebPageElement):
    """
A navigation element of the page.
    """
    class_: Literal['https://schema.org/SiteNavigationElement'] = Field( # type: ignore
        default='https://schema.org/SiteNavigationElement',
        alias='@type',
        serialization_alias='@type'
    )
