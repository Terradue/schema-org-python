from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class SheetMusic(CreativeWork):
    """
Printed music, as opposed to performed or recorded music.
    """
    type_: Literal['https://schema.org/SheetMusic'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SheetMusic'),serialization_alias='class') # type: ignore
