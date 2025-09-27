from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class TierBenefitEnumeration(Enumeration):
    """
An enumeration of possible benefits as part of a loyalty (members) program.
    """
    type_: Literal['https://schema.org/TierBenefitEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TierBenefitEnumeration'),serialization_alias='class') # type: ignore
