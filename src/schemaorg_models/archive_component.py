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
    from .place import Place
    from .postal_address import PostalAddress
    from .archive_organization import ArchiveOrganization

class ArchiveComponent(CreativeWork):
    """
An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.
    """
    class_: Literal['https://schema.org/ArchiveComponent'] = Field( # type: ignore
        default='https://schema.org/ArchiveComponent',
        alias='@type',
        serialization_alias='@type'
    )
    holdingArchive: Optional[Union["ArchiveOrganization", List["ArchiveOrganization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'holdingArchive',
            'https://schema.org/holdingArchive'
        ),
        serialization_alias='https://schema.org/holdingArchive'
    )
    itemLocation: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemLocation',
            'https://schema.org/itemLocation'
        ),
        serialization_alias='https://schema.org/itemLocation'
    )
