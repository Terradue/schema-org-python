from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class DepartmentStore(Store):
    """
A department store.
    """
    class_: Literal['https://schema.org/DepartmentStore'] = Field(default='https://schema.org/DepartmentStore', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
