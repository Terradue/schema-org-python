from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class QAPage(WebPage):
    """
A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs).
    """
    class_: Literal['https://schema.org/QAPage'] = Field(default='https://schema.org/QAPage', alias='@type', serialization_alias='@type') # type: ignore
