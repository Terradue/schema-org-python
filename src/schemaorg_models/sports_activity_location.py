from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """
A sub property of location. The sports activity location where this action occurred.
    """
    type_: Literal['https://schema.org/SportsActivityLocation'] = Field(default='https://schema.org/SportsActivityLocation', alias='@type', serialization_alias='@type') # type: ignore
