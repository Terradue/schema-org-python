from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.episode import Episode


class RadioEpisode(Episode):
    """
A radio episode which can be part of a series or season.
    """
    type_: Literal['https://schema.org/RadioEpisode'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadioEpisode'),serialization_alias='class') # type: ignore
