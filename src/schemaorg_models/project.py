from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .organization import Organization

class Project(Organization):
    '''
    An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim.
Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]] to indicate project sub-structures. 
   
    '''
    class_: Literal['https://schema.org/Project'] = Field( # type: ignore
        default='https://schema.org/Project',
        alias='@type',
        serialization_alias='@type'
    )
