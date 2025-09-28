from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.organization import Organization
from schemaorg_models.member_program_tier import MemberProgramTier

class MemberProgram(Intangible):
    """
A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits, for example better pricing, free shipping or returns, or the ability to earn loyalty points. Member programs may have multiple tiers, for example silver and gold members, each with different benefits.
    """
    class_: Literal['https://schema.org/MemberProgram'] = Field( # type: ignore
        default='https://schema.org/MemberProgram',
        alias='@type',
        serialization_alias='@type'
    )
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hostingOrganization',
            'https://schema.org/hostingOrganization'
        ),
        serialization_alias='https://schema.org/hostingOrganization'
    )
    hasTiers: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasTiers',
            'https://schema.org/hasTiers'
        ),
        serialization_alias='https://schema.org/hasTiers'
    )
