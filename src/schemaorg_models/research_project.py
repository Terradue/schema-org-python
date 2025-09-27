from typing import Literal
from pydantic import Field
from schemaorg_models.project import Project


class ResearchProject(Project):
    """
A Research project.
    """
    type_: Literal['https://schema.org/ResearchProject'] = Field(default='https://schema.org/ResearchProject', alias='@type', serialization_alias='@type') # type: ignore
