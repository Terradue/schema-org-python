from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Photograph(CreativeWork):
    """
A photograph.
    """
    class_: Literal['https://schema.org/Photograph'] = Field(default='https://schema.org/Photograph', alias='@type', serialization_alias='@type') # type: ignore
