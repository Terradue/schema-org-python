from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organize_action import OrganizeAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BookmarkAction(OrganizeAction):
    """
An agent bookmarks/flags/labels/tags/marks an object.
    """
    class_: Literal['https://schema.org/BookmarkAction'] = Field( # type: ignore
        default='https://schema.org/BookmarkAction',
        alias='@type',
        serialization_alias='@type'
    )
