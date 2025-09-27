from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class GamePlayMode(Enumeration):
    """
Indicates whether this game is multi-player, co-op or single-player.
    """
    class_: Literal['https://schema.org/GamePlayMode'] = Field(default='https://schema.org/GamePlayMode', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
