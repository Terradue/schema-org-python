from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class CollectionPage(WebPage):
    """
Web page type: Collection page.
    """
    type_: Literal['https://schema.org/CollectionPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CollectionPage'),serialization_alias='class') # type: ignore
