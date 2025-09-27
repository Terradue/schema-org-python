from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page_element import WebPageElement


class Table(WebPageElement):
    """
A table on a Web page.
    """
    type_: Literal['https://schema.org/Table'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Table'),serialization_alias='class') # type: ignore
