from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class OutletStore(Store):
    """
An outlet store.
    """
    class_: Literal['https://schema.org/OutletStore'] = Field(default='https://schema.org/OutletStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
