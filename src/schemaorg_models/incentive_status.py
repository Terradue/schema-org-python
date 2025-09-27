from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class IncentiveStatus(Enumeration):
    """
Enumerates a status for an incentive, such as whether it is active.
    """
    type_: Literal['https://schema.org/IncentiveStatus'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/IncentiveStatus'),serialization_alias='class') # type: ignore
