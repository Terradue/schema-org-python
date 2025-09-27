from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class ProfilePage(WebPage):
    """
Web page type: Profile page.
    """
    class_: Literal['https://schema.org/ProfilePage'] = Field('class', alias='class', serialization_alias='class') # type: ignore
