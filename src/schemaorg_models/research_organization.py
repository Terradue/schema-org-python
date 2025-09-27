from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class ResearchOrganization(Organization):
    """
A Research Organization (e.g. scientific institute, research company).
    """
    class_: Literal['https://schema.org/ResearchOrganization'] = Field(default='https://schema.org/ResearchOrganization', alias='class', serialization_alias='class') # type: ignore
