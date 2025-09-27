from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class Florist(Store):
    """
A florist.
    """
    type_: Literal['https://schema.org/Florist'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Florist'),serialization_alias='class') # type: ignore
