from __future__ import annotations

from .learning_resource import LearningResource    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Syllabus(LearningResource):
    """
A syllabus that describes the material covered in a course, often with several such sections per [[Course]] so that a distinct [[timeRequired]] can be provided for that section of the [[Course]].
    """
    class_: Literal['https://schema.org/Syllabus'] = Field( # type: ignore
        default='https://schema.org/Syllabus',
        alias='@type',
        serialization_alias='@type'
    )
