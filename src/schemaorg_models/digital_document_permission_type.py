from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """
A type of permission which can be granted for accessing a digital document.
    """
    type_: Literal['https://schema.org/DigitalDocumentPermissionType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DigitalDocumentPermissionType'),serialization_alias='class') # type: ignore
