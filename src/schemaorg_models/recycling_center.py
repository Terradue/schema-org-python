from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """
A recycling center.
    """
    class_: Literal['https://schema.org/RecyclingCenter'] = Field(default='https://schema.org/RecyclingCenter', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
