from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """
A recycling center.
    """
    class_: Literal['https://schema.org/RecyclingCenter'] = Field(default='https://schema.org/RecyclingCenter', alias='class', serialization_alias='class') # type: ignore
