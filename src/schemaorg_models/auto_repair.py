from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """
Car repair business.
    """
    type_: Literal['https://schema.org/AutoRepair'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutoRepair'),serialization_alias='class') # type: ignore
