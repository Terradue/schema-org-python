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
from .local_business import LocalBusiness

class MedicalBusiness(LocalBusiness):
    '''
    A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals.
    '''
    class_: Literal['https://schema.org/MedicalBusiness'] = Field( # type: ignore
        default='https://schema.org/MedicalBusiness',
        alias='@type',
        serialization_alias='@type'
    )
