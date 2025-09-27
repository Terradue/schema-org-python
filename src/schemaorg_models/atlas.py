from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Atlas(CreativeWork):
    """
A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.
    """
    type_: Literal['https://schema.org/Atlas'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Atlas'),serialization_alias='class') # type: ignore
