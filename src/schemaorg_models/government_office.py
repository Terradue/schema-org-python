from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class GovernmentOffice(LocalBusiness):
    """
A government office&#x2014;for example, an IRS or DMV office.
    """
    class_: Literal['https://schema.org/GovernmentOffice'] = Field(default='https://schema.org/GovernmentOffice', alias='class', serialization_alias='class') # type: ignore
