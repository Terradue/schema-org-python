from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Poster(CreativeWork):
    """
A large, usually printed placard, bill, or announcement, often illustrated, that is posted to advertise or publicize something.
    """
    type_: Literal['https://schema.org/Poster'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Poster'),serialization_alias='class') # type: ignore
