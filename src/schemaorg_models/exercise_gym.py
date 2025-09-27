from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """
A gym.
    """
    type_: Literal['https://schema.org/ExerciseGym'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ExerciseGym'),serialization_alias='class') # type: ignore
