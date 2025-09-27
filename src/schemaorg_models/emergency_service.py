from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class EmergencyService(LocalBusiness):
    """
An emergency service, such as a fire station or ER.
    """
    class_: Literal['https://schema.org/EmergencyService'] = Field(default='https://schema.org/EmergencyService', alias='@type', serialization_alias='@type') # type: ignore
