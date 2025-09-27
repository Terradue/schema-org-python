from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """
A recycling center.
    """
    type_: Literal['https://schema.org/RecyclingCenter'] = Field(default='https://schema.org/RecyclingCenter', alias='@type', serialization_alias='@type') # type: ignore
