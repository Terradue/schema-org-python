from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class QAPage(WebPage):
    """
A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question answering site or documenting Frequently Asked Questions (FAQs).
    """
    type_: Literal['https://schema.org/QAPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/QAPage'),serialization_alias='class') # type: ignore
