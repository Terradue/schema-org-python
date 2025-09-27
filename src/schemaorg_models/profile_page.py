from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class ProfilePage(WebPage):
    """
Web page type: Profile page.
    """
    type_: Literal['https://schema.org/ProfilePage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ProfilePage'),serialization_alias='class') # type: ignore
