from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """
A tourist information center.
    """
    class_: Literal['https://schema.org/TouristInformationCenter'] = Field(default='https://schema.org/TouristInformationCenter', alias='class', serialization_alias='class') # type: ignore
