from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class Store(LocalBusiness):
    """
A retail good store.
    """
    type_: Literal['https://schema.org/Store'] = Field(default='https://schema.org/Store', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
