from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organize_action import OrganizeAction

class BookmarkAction(OrganizeAction):
    """
An agent bookmarks/flags/labels/tags/marks an object.
    """
    class_: Literal['https://schema.org/BookmarkAction'] = Field( # type: ignore
        default='https://schema.org/BookmarkAction',
        alias='@type',
        serialization_alias='@type'
    )
