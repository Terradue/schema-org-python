from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class DigitalDocumentPermissionType(Enumeration):
    """
A type of permission which can be granted for accessing a digital document.
    """
    class_: Literal['https://schema.org/DigitalDocumentPermissionType'] = Field(default='https://schema.org/DigitalDocumentPermissionType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
