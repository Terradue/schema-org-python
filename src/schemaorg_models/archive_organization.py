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
from .local_business import LocalBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .archive_component import ArchiveComponent

class ArchiveOrganization(LocalBusiness):
    '''
    An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public.

    Attributes:
        archiveHeld: Collection, [fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept or maintained by an [[ArchiveOrganization]].
    '''
    class_: Literal['https://schema.org/ArchiveOrganization'] = Field( # type: ignore
        default='https://schema.org/ArchiveOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    archiveHeld: Optional[Union['ArchiveComponent', List['ArchiveComponent']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
