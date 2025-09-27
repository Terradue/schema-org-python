from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.resort import Resort


class SkiResort(Resort):
    """
A ski resort.
    """
    type_: Literal['https://schema.org/SkiResort'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SkiResort'),serialization_alias='class') # type: ignore
