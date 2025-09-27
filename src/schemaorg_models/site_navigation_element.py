from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page_element import WebPageElement


class SiteNavigationElement(WebPageElement):
    """
A navigation element of the page.
    """
    type_: Literal['https://schema.org/SiteNavigationElement'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SiteNavigationElement'),serialization_alias='class') # type: ignore
