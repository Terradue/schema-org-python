from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.project import Project


class ResearchProject(Project):
    """
A Research project.
    """
    type_: Literal['https://schema.org/ResearchProject'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ResearchProject'),serialization_alias='class') # type: ignore
