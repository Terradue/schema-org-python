from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """
An employment agency.
    """
    type_: Literal['https://schema.org/EmploymentAgency'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EmploymentAgency'),serialization_alias='class') # type: ignore
