from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Play(CreativeWork):
    """
A play is a form of literature, usually consisting of dialogue between characters, intended for theatrical performance rather than just reading. Note: A performance of a Play would be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].
    """
    type_: Literal['https://schema.org/Play'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Play'),serialization_alias='class') # type: ignore
