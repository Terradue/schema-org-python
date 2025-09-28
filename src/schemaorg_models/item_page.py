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

class ItemPage(WebPage):
    """
A page devoted to a single item, such as a particular product or hotel.
    """
    class_: Literal['https://schema.org/ItemPage'] = Field( # type: ignore
        default='https://schema.org/ItemPage',
        alias='@type',
        serialization_alias='@type'
    )
