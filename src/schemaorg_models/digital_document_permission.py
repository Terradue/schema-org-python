from __future__ import annotations
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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .digital_document_permission_type import DigitalDocumentPermissionType
    from .audience import Audience
    from .person import Person
    from .organization import Organization
    from .contact_point import ContactPoint

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
    grantee: Optional[Union["Organization", List["Organization"], "Audience", List["Audience"], "Person", List["Person"], "ContactPoint", List["ContactPoint"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'grantee',
            'https://schema.org/grantee'
        ),
        serialization_alias='https://schema.org/grantee'
    )
