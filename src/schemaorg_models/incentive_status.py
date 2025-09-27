from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveStatus(Enumeration):
    """
Enumerates a status for an incentive, such as whether it is active.
    """
    class_: Literal['https://schema.org/IncentiveStatus'] = Field('class', alias='class', serialization_alias='class') # type: ignore
