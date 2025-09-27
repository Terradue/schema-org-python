from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """
Car repair, sales, or parts.
    """
    type_: Literal['https://schema.org/AutomotiveBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AutomotiveBusiness'),serialization_alias='class') # type: ignore
