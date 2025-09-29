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
    from .place import Place
    from .archive_organization import ArchiveOrganization
    from .postal_address import PostalAddress

class ArchiveComponent(CreativeWork):
    '''
    An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.

    Attributes:
        holdingArchive: [[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].
        itemLocation: Current location of the item.
    '''
    class_: Literal['https://schema.org/ArchiveComponent'] = Field( # type: ignore
        default='https://schema.org/ArchiveComponent',
        alias='@type',
        serialization_alias='@type'
    )
    holdingArchive: Optional[Union['ArchiveOrganization', List['ArchiveOrganization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    itemLocation: Optional[Union['PostalAddress', List['PostalAddress'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
