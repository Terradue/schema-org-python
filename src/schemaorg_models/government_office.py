from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """
A government office&#x2014;for example, an IRS or DMV office.
    """
    type_: Literal['https://schema.org/GovernmentOffice'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GovernmentOffice'),serialization_alias='class') # type: ignore
