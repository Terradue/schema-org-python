from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class ShortStory(CreativeWork):
    """
Short story or tale. A brief work of literature, usually written in narrative prose.
    """
    class_: Literal['https://schema.org/ShortStory'] = Field('class', alias='class', serialization_alias='class') # type: ignore
