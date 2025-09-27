from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class SheetMusic(CreativeWork):
    """
Printed music, as opposed to performed or recorded music.
    """
    class_: Literal['https://schema.org/SheetMusic'] = Field('class', alias='class', serialization_alias='class') # type: ignore
