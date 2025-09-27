from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class BikeStore(Store):
    """
A bike store.
    """
    class_: Literal['https://schema.org/BikeStore'] = Field(default='https://schema.org/BikeStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
