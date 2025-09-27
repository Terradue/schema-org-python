from typing import Literal
from pydantic import Field
from schemaorg_models.physician import Physician


class PhysiciansOffice(Physician):
    """
A doctor's office or clinic.
    """
    class_: Literal['https://schema.org/PhysiciansOffice'] = Field('class', alias='class', serialization_alias='class') # type: ignore
