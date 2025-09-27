from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class MusicStore(Store):
    """
A music store.
    """
    class_: Literal['https://schema.org/MusicStore'] = Field(default='https://schema.org/MusicStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
