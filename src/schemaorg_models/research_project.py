from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .project import Project

class ResearchProject(Project):
    """
A Research project.
    """
    class_: Literal['https://schema.org/ResearchProject'] = Field( # type: ignore
        default='https://schema.org/ResearchProject',
        alias='@type',
        serialization_alias='@type'
    )
