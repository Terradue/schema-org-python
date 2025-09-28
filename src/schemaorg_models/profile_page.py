from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page import WebPage

class ProfilePage(WebPage):
    """
Web page type: Profile page.
    """
    class_: Literal['https://schema.org/ProfilePage'] = Field( # type: ignore
        default='https://schema.org/ProfilePage',
        alias='@type',
        serialization_alias='@type'
    )
