from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.service import Service


class Taxi(Service):
    """
A taxi.
    """
    type_: Literal['https://schema.org/Taxi'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Taxi'),serialization_alias='class') # type: ignore
