from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.learning_resource import LearningResource

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Quiz(LearningResource):
    """
Quiz: A test of knowledge, skills and abilities.
    """
    class_: Literal['https://schema.org/Quiz'] = Field( # type: ignore
        default='https://schema.org/Quiz',
        alias='@type',
        serialization_alias='@type'
    )
