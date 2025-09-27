from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class FAQPage(WebPage):
    """
A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]]).
    """
    type_: Literal['https://schema.org/FAQPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FAQPage'),serialization_alias='class') # type: ignore
