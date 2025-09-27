from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class DeliveryMethod(Enumeration):
    """
A sub property of instrument. The method of delivery.
    """
    type_: Literal['https://schema.org/DeliveryMethod'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DeliveryMethod'),serialization_alias='class') # type: ignore
