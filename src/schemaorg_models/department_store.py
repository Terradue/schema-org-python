from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class DepartmentStore(Store):
    """
A department store.
    """
    class_: Literal['https://schema.org/DepartmentStore'] = Field( # type: ignore
        default='https://schema.org/DepartmentStore',
        alias='@type',
        serialization_alias='@type'
    )
