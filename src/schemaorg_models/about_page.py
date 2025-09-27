from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class AboutPage(WebPage):
    """
Web page type: About page.
    """
    type_: Literal['https://schema.org/AboutPage'] = Field(default='https://schema.org/AboutPage', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
