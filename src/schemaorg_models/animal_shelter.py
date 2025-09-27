from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    class_: Literal['https://schema.org/AnimalShelter'] = Field(default='https://schema.org/AnimalShelter', alias='class', serialization_alias='class') # type: ignore
