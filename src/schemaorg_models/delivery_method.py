from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class DeliveryMethod(Enumeration):
    """
A sub property of instrument. The method of delivery.
    """
    class_: Literal['https://schema.org/DeliveryMethod'] = Field(default='https://schema.org/DeliveryMethod', alias='@type', serialization_alias='@type') # type: ignore
