from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """
A car wash business.
    """
    type_: Literal['https://schema.org/AutoWash'] = Field(default='https://schema.org/AutoWash', alias='@type', serialization_alias='@type') # type: ignore
