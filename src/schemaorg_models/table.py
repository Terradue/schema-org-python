from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .web_page_element import WebPageElement

class Table(WebPageElement):
    """
A table on a Web page.
    """
    class_: Literal['https://schema.org/Table'] = Field( # type: ignore
        default='https://schema.org/Table',
        alias='@type',
        serialization_alias='@type'
    )
