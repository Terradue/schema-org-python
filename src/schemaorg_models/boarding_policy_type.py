from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """
A type of boarding policy used by an airline.
    """
    class_: Literal['https://schema.org/BoardingPolicyType'] = Field(default='https://schema.org/BoardingPolicyType', alias='class', serialization_alias='class') # type: ignore
