from __future__ import annotations

from .web_page import WebPage    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CollectionPage(WebPage):
    """
Web page type: Collection page.
    """
    class_: Literal['https://schema.org/CollectionPage'] = Field( # type: ignore
        default='https://schema.org/CollectionPage',
        alias='@type',
        serialization_alias='@type'
    )
