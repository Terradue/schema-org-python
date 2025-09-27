from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    type_: Literal['https://schema.org/AnimalShelter'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AnimalShelter'),serialization_alias='class') # type: ignore
