from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.web_page import WebPage


class CheckoutPage(WebPage):
    """
Web page type: Checkout page.
    """
    type_: Literal['https://schema.org/CheckoutPage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CheckoutPage'),serialization_alias='class') # type: ignore
