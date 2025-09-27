from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.physician import Physician


class PhysiciansOffice(Physician):
    """
A doctor's office or clinic.
    """
    type_: Literal['https://schema.org/PhysiciansOffice'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PhysiciansOffice'),serialization_alias='class') # type: ignore
