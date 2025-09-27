from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class Store(LocalBusiness):
    """
A retail good store.
    """
    class_: Literal['https://schema.org/Store'] = Field(default='https://schema.org/Store', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
