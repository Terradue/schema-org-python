from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class SportingGoodsStore(Store):
    """
A sporting goods store.
    """
    class_: Literal['https://schema.org/SportingGoodsStore'] = Field(default='https://schema.org/SportingGoodsStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
