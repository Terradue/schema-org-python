from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.store import Store


class DepartmentStore(Store):
    """
A department store.
    """
    type_: Literal['https://schema.org/DepartmentStore'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DepartmentStore'),serialization_alias='class') # type: ignore
