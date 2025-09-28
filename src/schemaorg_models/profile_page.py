from __future__ import annotations

from .web_page import WebPage    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ProfilePage(WebPage):
    """
Web page type: Profile page.
    """
    class_: Literal['https://schema.org/ProfilePage'] = Field( # type: ignore
        default='https://schema.org/ProfilePage',
        alias='@type',
        serialization_alias='@type'
    )
