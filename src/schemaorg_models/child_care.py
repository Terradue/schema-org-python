from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class ChildCare(LocalBusiness):
    """
A Childcare center.
    """
    type_: Literal['https://schema.org/ChildCare'] = Field(default='https://schema.org/ChildCare', alias='@type', serialization_alias='@type') # type: ignore
