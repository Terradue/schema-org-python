from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Play(CreativeWork):
    """
A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading. Note: A performance of a Play would be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].
    """
    class_: Literal['https://schema.org/Play'] = Field(default='https://schema.org/Play', alias='class', serialization_alias='class') # type: ignore
