from __future__ import annotations

from .web_page_element import WebPageElement    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WPAdBlock(WebPageElement):
    """
An advertising section of the page.
    """
    class_: Literal['https://schema.org/WPAdBlock'] = Field( # type: ignore
        default='https://schema.org/WPAdBlock',
        alias='@type',
        serialization_alias='@type'
    )
