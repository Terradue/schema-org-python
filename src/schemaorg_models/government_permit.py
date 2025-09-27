from typing import Literal
from pydantic import Field
from schemaorg_models.permit import Permit


class GovernmentPermit(Permit):
    """
A permit issued by a government agency.
    """
    class_: Literal['https://schema.org/GovernmentPermit'] = Field(default='https://schema.org/GovernmentPermit', alias='class', serialization_alias='class') # type: ignore
