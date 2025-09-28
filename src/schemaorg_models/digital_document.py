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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .digital_document_permission import DigitalDocumentPermission

class DigitalDocument(CreativeWork):
    """
An electronic file or document.
    """
    class_: Literal['https://schema.org/DigitalDocument'] = Field( # type: ignore
        default='https://schema.org/DigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
    hasDigitalDocumentPermission: Optional[Union["DigitalDocumentPermission", List["DigitalDocumentPermission"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasDigitalDocumentPermission',
            'https://schema.org/hasDigitalDocumentPermission'
        ),
        serialization_alias='https://schema.org/hasDigitalDocumentPermission'
    )
