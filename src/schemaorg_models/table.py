from typing import Literal
from pydantic import Field
from schemaorg_models.web_page_element import WebPageElement


class Table(WebPageElement):
    """
A table on a Web page.
    """
    type_: Literal['https://schema.org/Table'] = Field(default='https://schema.org/Table', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
