from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PurchaseType(Enumeration):
    """
Optional. The type of purchase the consumer must make in order to qualify for this incentive.
    """
    class_: Literal['https://schema.org/PurchaseType'] = Field(default='https://schema.org/PurchaseType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
