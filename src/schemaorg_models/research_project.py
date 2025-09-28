from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.project import Project

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
