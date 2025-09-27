from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class SelfStorage(LocalBusiness):
    """
A self-storage facility.
    """
    type_: Literal['https://schema.org/SelfStorage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SelfStorage'),serialization_alias='class') # type: ignore
