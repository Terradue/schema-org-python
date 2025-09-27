from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """
A sub property of location. The entertainment business where the action occurred.
    """
    type_: Literal['https://schema.org/EntertainmentBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EntertainmentBusiness'),serialization_alias='class') # type: ignore
