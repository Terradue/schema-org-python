from typing import Literal
from pydantic import Field
from schemaorg_models.learning_resource import LearningResource


class Syllabus(LearningResource):
    """
A syllabus that describes the material covered in a course, often with several such sections per [[Course]] so that a distinct [[timeRequired]] can be provided for that section of the [[Course]].
    """
    type_: Literal['https://schema.org/Syllabus'] = Field(default='https://schema.org/Syllabus', alias='@type', serialization_alias='@type') # type: ignore
