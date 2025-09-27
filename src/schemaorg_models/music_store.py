from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MusicStore(Store):
    """
A music store.
    """
    type_: Literal['https://schema.org/MusicStore'] = Field(default='https://schema.org/MusicStore', alias='@type', serialization_alias='@type') # type: ignore
