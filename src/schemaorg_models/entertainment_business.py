from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """
A sub property of location. The entertainment business where the action occurred.
    """
    class_: Literal['https://schema.org/EntertainmentBusiness'] = Field(default='https://schema.org/EntertainmentBusiness', alias='class', serialization_alias='class') # type: ignore
