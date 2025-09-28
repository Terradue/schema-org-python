from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

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
from schemaorg_models.digital_document_permission import DigitalDocumentPermission

class DigitalDocument(CreativeWork):
    """
An electronic file or document.
    """
    class_: Literal['https://schema.org/DigitalDocument'] = Field( # type: ignore
        default='https://schema.org/DigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
    hasDigitalDocumentPermission: Optional[Union[DigitalDocumentPermission, List[DigitalDocumentPermission]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDigitalDocumentPermission',
            'https://schema.org/hasDigitalDocumentPermission'
        ),
        serialization_alias='https://schema.org/hasDigitalDocumentPermission'
    )
