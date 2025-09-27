from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class Florist(Store):
    """
A florist.
    """
    class_: Literal['https://schema.org/Florist'] = Field(default='https://schema.org/Florist', alias='class', serialization_alias='class') # type: ignore
