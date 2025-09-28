from __future__ import annotations

from .web_page import WebPage    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CheckoutPage(WebPage):
    """
Web page type: Checkout page.
    """
    class_: Literal['https://schema.org/CheckoutPage'] = Field( # type: ignore
        default='https://schema.org/CheckoutPage',
        alias='@type',
        serialization_alias='@type'
    )
