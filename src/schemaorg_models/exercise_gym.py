from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class ExerciseGym(SportsActivityLocation):
    """
A gym.
    """
    class_: Literal['https://schema.org/ExerciseGym'] = Field(default='https://schema.org/ExerciseGym', alias='@type', serialization_alias='@type') # type: ignore
