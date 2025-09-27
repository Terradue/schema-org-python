from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class ShortStory(CreativeWork):
    """
Short story or tale. A brief work of literature, usually written in narrative prose.
    """
    type_: Literal['https://schema.org/ShortStory'] = Field(default='https://schema.org/ShortStory', alias='@type', serialization_alias='@type') # type: ignore
