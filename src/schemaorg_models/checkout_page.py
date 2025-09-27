from typing import Literal
from pydantic import Field
from schemaorg_models.web_page import WebPage


class CheckoutPage(WebPage):
    """
Web page type: Checkout page.
    """
    class_: Literal['https://schema.org/CheckoutPage'] = Field(default='https://schema.org/CheckoutPage', alias='class', serialization_alias='class') # type: ignore
