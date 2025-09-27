from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """
A recycling center.
    """
    type_: Literal['https://schema.org/RecyclingCenter'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RecyclingCenter'),serialization_alias='class') # type: ignore
