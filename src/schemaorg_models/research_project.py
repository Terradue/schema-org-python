from typing import Literal
from pydantic import Field
from schemaorg_models.project import Project


class ResearchProject(Project):
    """
A Research project.
    """
    class_: Literal['https://schema.org/ResearchProject'] = Field('class', alias='class', serialization_alias='class') # type: ignore
