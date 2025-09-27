from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """
Car repair business.
    """
    type_: Literal['https://schema.org/AutoRepair'] = Field(default='https://schema.org/AutoRepair', alias='@type', serialization_alias='@type') # type: ignore
