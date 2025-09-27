from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """
An employment agency.
    """
    class_: Literal['https://schema.org/EmploymentAgency'] = Field(default='https://schema.org/EmploymentAgency', alias='@type', serialization_alias='@type') # type: ignore
