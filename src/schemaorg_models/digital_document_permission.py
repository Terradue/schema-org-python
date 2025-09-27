from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.organization import Organization
from schemaorg_models.audience import Audience
from schemaorg_models.person import Person

class DigitalDocumentPermission(Intangible):
    """
A permission for a particular person or group to access a particular file.
    """
    class_: Literal['https://schema.org/DigitalDocumentPermission'] = Field(default='https://schema.org/DigitalDocumentPermission', alias='@type', serialization_alias='@type') # type: ignore
    permissionType: Optional[Union["DigitalDocumentPermissionType", List["DigitalDocumentPermissionType"]]] = Field(default=None, validation_alias=AliasChoices('permissionType', 'https://schema.org/permissionType'), serialization_alias='https://schema.org/permissionType')
    grantee: Optional[Union[Organization, List[Organization], Audience, List[Audience], Person, List[Person], "ContactPoint", List["ContactPoint"]]] = Field(default=None, validation_alias=AliasChoices('grantee', 'https://schema.org/grantee'), serialization_alias='https://schema.org/grantee')
