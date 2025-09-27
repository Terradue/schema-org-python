from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class TierBenefitEnumeration(Enumeration):
    """
An enumeration of possible benefits as part of a loyalty (members) program.
    """
    type_: Literal['https://schema.org/TierBenefitEnumeration'] = Field(default='https://schema.org/TierBenefitEnumeration', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
