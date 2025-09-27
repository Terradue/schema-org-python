from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class SearchRescueOrganization(Organization):
    """
A Search and Rescue organization of some kind.
    """
    type_: Literal['https://schema.org/SearchRescueOrganization'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SearchRescueOrganization'),serialization_alias='class') # type: ignore
