from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    class_: Literal['https://schema.org/AnimalShelter'] = Field(default='https://schema.org/AnimalShelter', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
