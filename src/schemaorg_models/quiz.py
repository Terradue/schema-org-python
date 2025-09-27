from typing import Literal
from pydantic import Field
from schemaorg_models.learning_resource import LearningResource


class Quiz(LearningResource):
    """
Quiz: A test of knowledge, skills and abilities.
    """
    class_: Literal['https://schema.org/Quiz'] = Field(default='https://schema.org/Quiz', alias='class', serialization_alias='class') # type: ignore
