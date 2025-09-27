from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """
A type of permission which can be granted for accessing a digital document.
    """
    type_: Literal['https://schema.org/DigitalDocumentPermissionType'] = Field(default='https://schema.org/DigitalDocumentPermissionType', alias='@type', serialization_alias='@type') # type: ignore
