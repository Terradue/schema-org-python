from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    class_: Literal['https://schema.org/AnimalShelter'] = Field('class', alias='class', serialization_alias='class') # type: ignore
