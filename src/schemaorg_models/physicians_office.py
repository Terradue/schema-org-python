from typing import Literal
from pydantic import Field
from schemaorg_models.physician import Physician


class PhysiciansOffice(Physician):
    """
A doctor's office or clinic.
    """
    type_: Literal['https://schema.org/PhysiciansOffice'] = Field(default='https://schema.org/PhysiciansOffice', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
