from typing import Literal
from pydantic import Field
from schemaorg_models.resort import Resort


class SkiResort(Resort):
    """
A ski resort.
    """
    class_: Literal['https://schema.org/SkiResort'] = Field(default='https://schema.org/SkiResort', alias='class', serialization_alias='class') # type: ignore
