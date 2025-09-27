from typing import Literal
from pydantic import Field
from schemaorg_models.learning_resource import LearningResource


class Syllabus(LearningResource):
    """
A syllabus that describes the material covered in a course, often with several such sections per [[Course]] so that a distinct [[timeRequired]] can be provided for that section of the [[Course]].
    """
    class_: Literal['https://schema.org/Syllabus'] = Field(default='https://schema.org/Syllabus', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
