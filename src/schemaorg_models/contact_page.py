from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ContactPage(WebPage):
    """
Web page type: Contact page.
    """
    class_: Literal['https://schema.org/ContactPage'] = Field(default='https://schema.org/ContactPage', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
