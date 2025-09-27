from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """
A tourist information center.
    """
    type_: Literal['https://schema.org/TouristInformationCenter'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TouristInformationCenter'),serialization_alias='class') # type: ignore
