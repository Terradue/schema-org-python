from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Sculpture(CreativeWork):
    """
A piece of sculpture.
    """
    class_: Literal['https://schema.org/Sculpture'] = Field(default='https://schema.org/Sculpture', alias='@type', serialization_alias='@type') # type: ignore
