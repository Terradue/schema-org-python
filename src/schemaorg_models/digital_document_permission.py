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
from schemaorg_models.audience import Audience
from schemaorg_models.person import Person

class DigitalDocumentPermission(Intangible):
    """
A permission for a particular person or group to access a particular file.
    """
    class_: Literal['https://schema.org/DigitalDocumentPermission'] = Field( # type: ignore
        default='https://schema.org/DigitalDocumentPermission',
        alias='@type',
        serialization_alias='@type'
    )
    permissionType: Optional[Union["DigitalDocumentPermissionType", List["DigitalDocumentPermissionType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'permissionType',
            'https://schema.org/permissionType'
        ),
        serialization_alias='https://schema.org/permissionType'
    )
    grantee: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person], "ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'grantee',
            'https://schema.org/grantee'
        ),
        serialization_alias='https://schema.org/grantee'
    )
