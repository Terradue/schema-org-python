from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ProfilePage(WebPage):
    """
Web page type: Profile page.
    """
    class_: Literal['https://schema.org/ProfilePage'] = Field(default='https://schema.org/ProfilePage', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
