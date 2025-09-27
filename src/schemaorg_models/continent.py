from typing import Literal
from pydantic import Field
from schemaorg_models.landform import Landform


class Continent(Landform):
    """
One of the continents (for example, Europe or Africa).
    """
    class_: Literal['https://schema.org/Continent'] = Field('class', alias='class', serialization_alias='class') # type: ignore
