from typing import Literal
from pydantic import Field
from schemaorg_models.learning_resource import LearningResource


class Quiz(LearningResource):
    """
Quiz: A test of knowledge, skills and abilities.
    """
    type_: Literal['https://schema.org/Quiz'] = Field(default='https://schema.org/Quiz', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
