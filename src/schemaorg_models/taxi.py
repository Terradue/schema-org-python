from typing import Literal
from pydantic import Field
from schemaorg_models.service import Service


class Taxi(Service):
    """
A taxi.
    """
    class_: Literal['https://schema.org/Taxi'] = Field(default='https://schema.org/Taxi', alias='class', serialization_alias='class') # type: ignore
