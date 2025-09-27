from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """
A type of boarding policy used by an airline.
    """
    type_: Literal['https://schema.org/BoardingPolicyType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BoardingPolicyType'),serialization_alias='class') # type: ignore
