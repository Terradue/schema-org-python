from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ContactPage(WebPage):
    """
Web page type: Contact page.
    """
    type_: Literal['https://schema.org/ContactPage'] = Field(default='https://schema.org/ContactPage', alias='@type', serialization_alias='@type') # type: ignore
