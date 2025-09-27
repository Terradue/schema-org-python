from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class Library(LocalBusiness):
    """
A library.
    """
    type_: Literal['https://schema.org/Library'] = Field(default='https://schema.org/Library', alias='@type', serialization_alias='@type') # type: ignore
