from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organize_action import OrganizeAction


class BookmarkAction(OrganizeAction):
    """
An agent bookmarks/flags/labels/tags/marks an object.
    """
    type_: Literal['https://schema.org/BookmarkAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BookmarkAction'),serialization_alias='class') # type: ignore
