from typing import Literal
from pydantic import Field
from schemaorg_models.landform import Landform


class Mountain(Landform):
    """
A mountain, like Mount Whitney or Mount Everest.
    """
    class_: Literal['https://schema.org/Mountain'] = Field('class', alias='class', serialization_alias='class') # type: ignore
