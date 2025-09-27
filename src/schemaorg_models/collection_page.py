from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class CollectionPage(WebPage):
    """
Web page type: Collection page.
    """
    class_: Literal['https://schema.org/CollectionPage'] = Field('class', alias='class', serialization_alias='class') # type: ignore
