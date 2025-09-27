from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class Language(Intangible):
    """
A sub property of instrument. The language used on this action.
    """
    class_: Literal['https://schema.org/Language'] = Field('class', alias='class', serialization_alias='class') # type: ignore
