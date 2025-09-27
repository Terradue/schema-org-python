from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """
Car repair business.
    """
    class_: Literal['https://schema.org/AutoRepair'] = Field(default='https://schema.org/AutoRepair', alias='class', serialization_alias='class') # type: ignore
