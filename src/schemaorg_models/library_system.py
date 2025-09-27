from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class LibrarySystem(Organization):
    """
A [[LibrarySystem]] is a collaborative system amongst several libraries.
    """
    class_: Literal['https://schema.org/LibrarySystem'] = Field(default='https://schema.org/LibrarySystem', alias='@type', serialization_alias='@type') # type: ignore
