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
from .local_business import LocalBusiness
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .archive_component import ArchiveComponent

class ArchiveOrganization(LocalBusiness):
    """
An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public.
    """
    class_: Literal['https://schema.org/ArchiveOrganization'] = Field( # type: ignore
        default='https://schema.org/ArchiveOrganization',
        alias='@type',
        serialization_alias='@type'
    )
    archiveHeld: Optional[Union[ArchiveComponent, List[ArchiveComponent]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'archiveHeld',
            'https://schema.org/archiveHeld'
        ),
        serialization_alias='https://schema.org/archiveHeld'
    )
