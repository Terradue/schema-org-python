from typing import Literal
from pydantic import Field
from schemaorg_models.store import Store


class ComputerStore(Store):
    """
A computer store.
    """
    class_: Literal['https://schema.org/ComputerStore'] = Field(default='https://schema.org/ComputerStore', alias='class', serialization_alias='class') # type: ignore
