from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ContactPage(WebPage):
    """
Web page type: Contact page.
    """
    class_: Literal['https://schema.org/ContactPage'] = Field('class', alias='class', serialization_alias='class') # type: ignore
