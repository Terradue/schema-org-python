from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class PurchaseType(Enumeration):
    """
Optional. The type of purchase the consumer must make in order to qualify for this incentive.
    """
    type_: Literal['https://schema.org/PurchaseType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PurchaseType'),serialization_alias='class') # type: ignore
