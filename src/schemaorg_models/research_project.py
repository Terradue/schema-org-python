from typing import Literal
from pydantic import Field
from schemaorg_models.project import Project


class ResearchProject(Project):
    """
A Research project.
    """
    class_: Literal['https://schema.org/ResearchProject'] = Field(default='https://schema.org/ResearchProject', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
