from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class TierBenefitEnumeration(Enumeration):
    """
An enumeration of possible benefits as part of a loyalty (members) program.
    """
    type_: Literal['https://schema.org/TierBenefitEnumeration'] = Field(default='https://schema.org/TierBenefitEnumeration', alias='@type', serialization_alias='@type') # type: ignore
