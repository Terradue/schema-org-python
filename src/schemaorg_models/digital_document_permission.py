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
from .contact_point import ContactPoint
from .person import Person
from .digital_document_permission_type import DigitalDocumentPermissionType
from .intangible import Intangible
from .organization import Organization
from .audience import Audience

class DigitalDocumentPermission(Intangible):
    """
A permission for a particular person or group to access a particular file.
    """
    class_: Literal['https://schema.org/DigitalDocumentPermission'] = Field( # type: ignore
        default='https://schema.org/DigitalDocumentPermission',
        alias='@type',
        serialization_alias='@type'
    )
    permissionType: Optional[Union[DigitalDocumentPermissionType, List[DigitalDocumentPermissionType]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'permissionType',
            'https://schema.org/permissionType'
        ),
        serialization_alias='https://schema.org/permissionType'
    )
    grantee: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person], ContactPoint, List[ContactPoint]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'grantee',
            'https://schema.org/grantee'
        ),
        serialization_alias='https://schema.org/grantee'
    )
