from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class IncentiveStatus(Enumeration):
    """
Enumerates a status for an incentive, such as whether it is active.
    """
    type_: Literal['https://schema.org/IncentiveStatus'] = Field(default='https://schema.org/IncentiveStatus', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
