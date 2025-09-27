from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class PurchaseType(Enumeration):
    """
Optional. The type of purchase the consumer must make in order to qualify for this incentive.
    """
    class_: Literal['https://schema.org/PurchaseType'] = Field(default='https://schema.org/PurchaseType', alias='class', serialization_alias='class') # type: ignore
