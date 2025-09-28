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

class QAPage(WebPage):
    """
A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs).
    """
    class_: Literal['https://schema.org/QAPage'] = Field( # type: ignore
        default='https://schema.org/QAPage',
        alias='@type',
        serialization_alias='@type'
    )
