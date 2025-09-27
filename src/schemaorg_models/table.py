from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class Table(WebPageElement):
    """
A table on a Web page.
    """
    type_: Literal['https://schema.org/Table'] = Field(default='https://schema.org/Table', alias='@type', serialization_alias='@type') # type: ignore
