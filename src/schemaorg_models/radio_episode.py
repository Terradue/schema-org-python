from typing import Literal
from pydantic import Field
from schemaorg_models.episode import Episode


class RadioEpisode(Episode):
    """
A radio episode which can be part of a series or season.
    """
    class_: Literal['https://schema.org/RadioEpisode'] = Field(default='https://schema.org/RadioEpisode', alias='@type', serialization_alias='@type') # type: ignore
