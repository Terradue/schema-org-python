from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class MusicStore(Store):
    """
A music store.
    """
    type_: Literal['https://schema.org/MusicStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MusicStore'),serialization_alias='class') # type: ignore
