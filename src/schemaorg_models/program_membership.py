from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .quantitative_value import QuantitativeValue
    from .organization import Organization
    from .member_program import MemberProgram

class ProgramMembership(Intangible):
    '''
    Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

    Attributes:
        programName: The program providing the membership. It is preferable to use [:program](https://schema.org/program) instead.
        members: A member of this organization.
        program: The [MemberProgram](https://schema.org/MemberProgram) associated with a [ProgramMembership](https://schema.org/ProgramMembership).
        membershipPointsEarned: The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)
        membershipNumber: A unique identifier for the membership.
        member: A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.
        hostingOrganization: The Organization (airline, travelers' club, retailer, etc.) the membership is made with or which offers the  MemberProgram.
    '''
    class_: Literal['https://schema.org/ProgramMembership'] = Field( # type: ignore
        default='https://schema.org/ProgramMembership',
        alias='@type',
        serialization_alias='@type'
    )
    programName: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programName',
            'https://schema.org/programName'
        ),
        serialization_alias='https://schema.org/programName'
    )
    members: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'members',
            'https://schema.org/members'
        ),
        serialization_alias='https://schema.org/members'
    )
    program: Optional[Union['MemberProgram', List['MemberProgram']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'program',
            'https://schema.org/program'
        ),
        serialization_alias='https://schema.org/program'
    )
    membershipPointsEarned: Optional[Union['QuantitativeValue', List['QuantitativeValue'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipPointsEarned',
            'https://schema.org/membershipPointsEarned'
        ),
        serialization_alias='https://schema.org/membershipPointsEarned'
    )
    membershipNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'membershipNumber',
            'https://schema.org/membershipNumber'
        ),
        serialization_alias='https://schema.org/membershipNumber'
    )
    member: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'member',
            'https://schema.org/member'
        ),
        serialization_alias='https://schema.org/member'
    )
    hostingOrganization: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hostingOrganization',
            'https://schema.org/hostingOrganization'
        ),
        serialization_alias='https://schema.org/hostingOrganization'
    )
