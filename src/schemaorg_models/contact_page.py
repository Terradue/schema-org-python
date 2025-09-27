from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class ContactPage(WebPage):
    """
Web page type: Contact page.
    """
    type_: Literal['https://schema.org/ContactPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ContactPage'),serialization_alias='class') # type: ignore
