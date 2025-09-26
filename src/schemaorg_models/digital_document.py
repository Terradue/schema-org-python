from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.digital_document_permission import DigitalDocumentPermission

class DigitalDocument(CreativeWork):
    """
An electronic file or document.
    """
    hasDigitalDocumentPermission: Optional[Union[DigitalDocumentPermission, List[DigitalDocumentPermission]]] = Field(default=None,validation_alias=AliasChoices('hasDigitalDocumentPermission', 'https://schema.org/hasDigitalDocumentPermission'),serialization_alias='https://schema.org/hasDigitalDocumentPermission')
