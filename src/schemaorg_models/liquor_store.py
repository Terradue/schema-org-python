from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class LiquorStore(Store):
    """
A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    """
    type_: Literal['https://schema.org/LiquorStore'] = Field(default='https://schema.org/LiquorStore', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
