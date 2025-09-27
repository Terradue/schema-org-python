from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class DepartmentStore(Store):
    """
A department store.
    """
    type_: Literal['https://schema.org/DepartmentStore'] = Field(default='https://schema.org/DepartmentStore', alias='@type', serialization_alias='@type') # type: ignore
