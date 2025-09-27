from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    type_: Literal['https://schema.org/AnimalShelter'] = Field(default='https://schema.org/AnimalShelter', alias='@type', serialization_alias='@type') # type: ignore
