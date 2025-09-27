from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person

class ProgramMembership(Intangible):
    """
Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.
    """
    type_: Literal['https://schema.org/ProgramMembership'] = Field(default='https://schema.org/ProgramMembership', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    programName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('programName', 'https://schema.org/programName'), serialization_alias='https://schema.org/programName')
    members: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('members', 'https://schema.org/members'), serialization_alias='https://schema.org/members')
    program: Optional[Union["MemberProgram", List["MemberProgram"]]] = Field(default=None, validation_alias=AliasChoices('program', 'https://schema.org/program'), serialization_alias='https://schema.org/program')
    membershipPointsEarned: Optional[Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('membershipPointsEarned', 'https://schema.org/membershipPointsEarned'), serialization_alias='https://schema.org/membershipPointsEarned')
    membershipNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('membershipNumber', 'https://schema.org/membershipNumber'), serialization_alias='https://schema.org/membershipNumber')
    member: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('member', 'https://schema.org/member'), serialization_alias='https://schema.org/member')
    hostingOrganization: Optional[Union[Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('hostingOrganization', 'https://schema.org/hostingOrganization'), serialization_alias='https://schema.org/hostingOrganization')
