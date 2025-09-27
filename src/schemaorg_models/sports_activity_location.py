from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """
A sub property of location. The sports activity location where this action occurred.
    """
    class_: Literal['https://schema.org/SportsActivityLocation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
