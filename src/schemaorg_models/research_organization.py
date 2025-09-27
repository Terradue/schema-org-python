from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class ResearchOrganization(Organization):
    """
A Research Organization (e.g. scientific institute, research company).
    """
    type_: Literal['https://schema.org/ResearchOrganization'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ResearchOrganization'),serialization_alias='class') # type: ignore
