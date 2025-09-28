from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page import WebPage

class CollectionPage(WebPage):
    """
Web page type: Collection page.
    """
    class_: Literal['https://schema.org/CollectionPage'] = Field( # type: ignore
        default='https://schema.org/CollectionPage',
        alias='@type',
        serialization_alias='@type'
    )
