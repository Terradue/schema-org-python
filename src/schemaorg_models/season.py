from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Season(CreativeWork):
    """
A season in a media series.
    """
    type_: Literal['https://schema.org/Season'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Season'),serialization_alias='class') # type: ignore
