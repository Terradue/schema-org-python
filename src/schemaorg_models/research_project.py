from __future__ import annotations

from .project import Project    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ResearchProject(Project):
    """
A Research project.
    """
    class_: Literal['https://schema.org/ResearchProject'] = Field( # type: ignore
        default='https://schema.org/ResearchProject',
        alias='@type',
        serialization_alias='@type'
    )
