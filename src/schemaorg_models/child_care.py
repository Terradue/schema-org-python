from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class ChildCare(LocalBusiness):
    """
A Childcare center.
    """
    type_: Literal['https://schema.org/ChildCare'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ChildCare'),serialization_alias='class') # type: ignore
