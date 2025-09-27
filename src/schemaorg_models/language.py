from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class Language(Intangible):
    """
A sub property of instrument. The language used on this action.
    """
    type_: Literal['https://schema.org/Language'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Language'),serialization_alias='class') # type: ignore
