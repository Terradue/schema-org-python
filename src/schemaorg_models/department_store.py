from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class DepartmentStore(Store):
    """
A department store.
    """
    class_: Literal['https://schema.org/DepartmentStore'] = Field('class', alias='class', serialization_alias='class') # type: ignore
