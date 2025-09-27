from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Painting(CreativeWork):
    """
A painting.
    """
    class_: Literal['https://schema.org/Painting'] = Field(default='https://schema.org/Painting', alias='@type', serialization_alias='@type') # type: ignore
