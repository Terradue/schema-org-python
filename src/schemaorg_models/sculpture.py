from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Sculpture(CreativeWork):
    """
A piece of sculpture.
    """
    class_: Literal['https://schema.org/Sculpture'] = Field('class', alias='class', serialization_alias='class') # type: ignore
