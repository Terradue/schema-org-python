from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.learning_resource import LearningResource


class Quiz(LearningResource):
    """
Quiz: A test of knowledge, skills and abilities.
    """
    type_: Literal['https://schema.org/Quiz'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Quiz'),serialization_alias='class') # type: ignore
