from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """
A car wash business.
    """
    class_: Literal['https://schema.org/AutoWash'] = Field(default='https://schema.org/AutoWash', alias='class', serialization_alias='class') # type: ignore
