from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class FAQPage(WebPage):
    """
A [[FAQPage]] is a [[WebPage]] presenting one or more "[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)" (see also [[QAPage]]).
    """
    class_: Literal['https://schema.org/FAQPage'] = Field(default='https://schema.org/FAQPage', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
