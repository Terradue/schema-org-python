from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """
A list of possible conditions for the item.
    """
    class_: Literal['https://schema.org/OfferItemCondition'] = Field(default='https://schema.org/OfferItemCondition', alias='class', serialization_alias='class') # type: ignore
