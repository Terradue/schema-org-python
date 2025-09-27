from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """
A list of possible conditions for the item.
    """
    type_: Literal['https://schema.org/OfferItemCondition'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OfferItemCondition'),serialization_alias='class') # type: ignore
