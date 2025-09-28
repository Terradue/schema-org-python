from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.article import Article

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class TechArticle(Article):
    """
A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.
    """
    class_: Literal['https://schema.org/TechArticle'] = Field( # type: ignore
        default='https://schema.org/TechArticle',
        alias='@type',
        serialization_alias='@type'
    )
    proficiencyLevel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'proficiencyLevel',
            'https://schema.org/proficiencyLevel'
        ),
        serialization_alias='https://schema.org/proficiencyLevel'
    )
    dependencies: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dependencies',
            'https://schema.org/dependencies'
        ),
        serialization_alias='https://schema.org/dependencies'
    )
