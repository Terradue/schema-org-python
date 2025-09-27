from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ProfilePage(WebPage):
    """
Web page type: Profile page.
    """
    class_: Literal['https://schema.org/ProfilePage'] = Field(default='https://schema.org/ProfilePage', alias='@type', serialization_alias='@type') # type: ignore
