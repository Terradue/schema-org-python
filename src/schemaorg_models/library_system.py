from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class LibrarySystem(Organization):
    """
A [[LibrarySystem]] is a collaborative system amongst several libraries.
    """
    type_: Literal['https://schema.org/LibrarySystem'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LibrarySystem'),serialization_alias='class') # type: ignore
