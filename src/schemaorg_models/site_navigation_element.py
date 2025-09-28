from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.web_page_element import WebPageElement

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
