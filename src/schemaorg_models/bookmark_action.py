from typing import Literal
from pydantic import Field
from schemaorg_models.organize_action import OrganizeAction


class BookmarkAction(OrganizeAction):
    """
An agent bookmarks/flags/labels/tags/marks an object.
    """
    type_: Literal['https://schema.org/BookmarkAction'] = Field(default='https://schema.org/BookmarkAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
