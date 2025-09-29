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
from .enumeration import Enumeration

class WarrantyScope(Enumeration):
    '''
    A range of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.\
\
Commonly used values:\
\
* http://purl.org/goodrelations/v1#Labor-BringIn\
* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn\
* http://purl.org/goodrelations/v1#PartsAndLabor-PickUp
      
    '''
    class_: Literal['https://schema.org/WarrantyScope'] = Field( # type: ignore
        default='https://schema.org/WarrantyScope',
        alias='@type',
        serialization_alias='@type'
    )
