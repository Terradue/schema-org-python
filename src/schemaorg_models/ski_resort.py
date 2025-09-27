from typing import Literal
from pydantic import Field
from schemaorg_models.resort import Resort


class SkiResort(Resort):
    """
A ski resort.
    """
    type_: Literal['https://schema.org/SkiResort'] = Field(default='https://schema.org/SkiResort', alias='@type', serialization_alias='@type') # type: ignore
