from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.permit import Permit


class GovernmentPermit(Permit):
    """
A permit issued by a government agency.
    """
    type_: Literal['https://schema.org/GovernmentPermit'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GovernmentPermit'),serialization_alias='class') # type: ignore
