from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class Library(LocalBusiness):
    """
A library.
    """
    class_: Literal['https://schema.org/Library'] = Field(default='https://schema.org/Library', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
