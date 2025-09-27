from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Poster(CreativeWork):
    """
A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.
    """
    class_: Literal['https://schema.org/Poster'] = Field(default='https://schema.org/Poster', alias='@type', serialization_alias='@type') # type: ignore
