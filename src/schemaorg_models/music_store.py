from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MusicStore(Store):
    """
A music store.
    """
    class_: Literal['https://schema.org/MusicStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
