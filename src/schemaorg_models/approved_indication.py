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
from .medical_indication import MedicalIndication

class ApprovedIndication(MedicalIndication):
    '''
    An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.
    '''
    class_: Literal['https://schema.org/ApprovedIndication'] = Field( # type: ignore
        default='https://schema.org/ApprovedIndication',
        alias='@type',
        serialization_alias='@type'
    )
