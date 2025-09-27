from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class DeliveryMethod(Enumeration):
    """
A sub property of instrument. The method of delivery.
    """
    class_: Literal['https://schema.org/DeliveryMethod'] = Field(default='https://schema.org/DeliveryMethod', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
