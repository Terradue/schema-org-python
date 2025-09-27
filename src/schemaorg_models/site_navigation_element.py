from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class SiteNavigationElement(WebPageElement):
    """
A navigation element of the page.
    """
    class_: Literal['https://schema.org/SiteNavigationElement'] = Field(default='https://schema.org/SiteNavigationElement', alias='class', serialization_alias='class') # type: ignore
