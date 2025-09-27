from typing import Literal
from pydantic import Field
from schemaorg_models.landform import Landform


class Volcano(Landform):
    """
A volcano, like Fujisan.
    """
    class_: Literal['https://schema.org/Volcano'] = Field(default='https://schema.org/Volcano', alias='@type', serialization_alias='@type') # type: ignore
