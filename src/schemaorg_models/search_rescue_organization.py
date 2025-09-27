from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class SearchRescueOrganization(Organization):
    """
A Search and Rescue organization of some kind.
    """
    type_: Literal['https://schema.org/SearchRescueOrganization'] = Field(default='https://schema.org/SearchRescueOrganization', alias='@type', serialization_alias='@type') # type: ignore
