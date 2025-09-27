from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class ShortStory(CreativeWork):
    """
Short story or tale. A brief work of literature, usually written in narrative prose.
    """
    type_: Literal['https://schema.org/ShortStory'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ShortStory'),serialization_alias='class') # type: ignore
