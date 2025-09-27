from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class Language(Intangible):
    """
A sub property of instrument. The language used on this action.
    """
    type_: Literal['https://schema.org/Language'] = Field(default='https://schema.org/Language', alias='@type', serialization_alias='@type') # type: ignore
