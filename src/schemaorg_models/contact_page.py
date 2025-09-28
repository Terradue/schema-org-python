from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.web_page import WebPage

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ContactPage(WebPage):
    """
Web page type: Contact page.
    """
    class_: Literal['https://schema.org/ContactPage'] = Field( # type: ignore
        default='https://schema.org/ContactPage',
        alias='@type',
        serialization_alias='@type'
    )
