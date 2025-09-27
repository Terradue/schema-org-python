from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class Florist(Store):
    """
A florist.
    """
    type_: Literal['https://schema.org/Florist'] = Field(default='https://schema.org/Florist', alias='@type', serialization_alias='@type') # type: ignore
