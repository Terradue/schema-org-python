from typing import Literal
from pydantic import Field
from schemaorg_models.organize_action import OrganizeAction


class BookmarkAction(OrganizeAction):
    """
An agent bookmarks/flags/labels/tags/marks an object.
    """
    class_: Literal['https://schema.org/BookmarkAction'] = Field(default='https://schema.org/BookmarkAction', alias='class', serialization_alias='class') # type: ignore
