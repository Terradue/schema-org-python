from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    An electronic file or document.

    Attributes:
        hasDigitalDocumentPermission: A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".
    '''
    class_: Literal['https://schema.org/DigitalDocument'] = Field( # type: ignore
        default='https://schema.org/DigitalDocument',
        alias='@type',
        serialization_alias='@type'
    )
    hasDigitalDocumentPermission: Optional[Union['DigitalDocumentPermission', List['DigitalDocumentPermission']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
