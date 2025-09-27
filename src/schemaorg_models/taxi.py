from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class Taxi(Service):
    """
A taxi.
    """
    type_: Literal['https://schema.org/Taxi'] = Field(default='https://schema.org/Taxi', alias='@type', serialization_alias='@type') # type: ignore
