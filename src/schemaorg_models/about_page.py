from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class AboutPage(WebPage):
    """
Web page type: About page.
    """
    type_: Literal['https://schema.org/AboutPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AboutPage'),serialization_alias='class') # type: ignore
