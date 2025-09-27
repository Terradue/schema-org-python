from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class EmergencyService(LocalBusiness):
    """
An emergency service, such as a fire station or ER.
    """
    type_: Literal['https://schema.org/EmergencyService'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EmergencyService'),serialization_alias='class') # type: ignore
