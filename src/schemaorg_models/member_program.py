from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.organization import Organization
from schemaorg_models.member_program_tier import MemberProgramTier

class MemberProgram(Intangible):
    """
A MemberProgram defines a loyalty (or membership) program that provides its members with certain benefits, for example better pricing, free shipping or returns, or the ability to earn loyalty points. Member programs may have multiple tiers, for example silver and gold members, each with different benefits.
    """
    class_: Literal['https://schema.org/MemberProgram'] = Field(default='https://schema.org/MemberProgram', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('hostingOrganization', 'https://schema.org/hostingOrganization'), serialization_alias='https://schema.org/hostingOrganization')
    hasTiers: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(default=None, validation_alias=AliasChoices('hasTiers', 'https://schema.org/hasTiers'), serialization_alias='https://schema.org/hasTiers')
