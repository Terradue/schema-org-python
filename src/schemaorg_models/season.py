from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Season(CreativeWork):
    """
A season in a media series.
    """
    class_: Literal['https://schema.org/Season'] = Field(default='https://schema.org/Season', alias='class', serialization_alias='class') # type: ignore
