from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.audience import Audience


class Researcher(Audience):
    """
Researchers.
    """
    type_: Literal['https://schema.org/Researcher'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Researcher'),serialization_alias='class') # type: ignore
