from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """
A sub property of location. The sports activity location where this action occurred.
    """
    type_: Literal['https://schema.org/SportsActivityLocation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SportsActivityLocation'),serialization_alias='class') # type: ignore
