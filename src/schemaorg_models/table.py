from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class Table(WebPageElement):
    """
A table on a Web page.
    """
    class_: Literal['https://schema.org/Table'] = Field('class', alias='class', serialization_alias='class') # type: ignore
