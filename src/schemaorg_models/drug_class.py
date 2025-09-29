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
from .medical_entity import MedicalEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .drug import Drug

class DrugClass(MedicalEntity):
    '''
    A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.

    Attributes:
        drug: Specifying a drug or medicine used in a medication procedure.
    '''
    class_: Literal['https://schema.org/DrugClass'] = Field( # type: ignore
        default='https://schema.org/DrugClass',
        alias='@type',
        serialization_alias='@type'
    )
    drug: Optional[Union['Drug', List['Drug']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drug',
            'https://schema.org/drug'
        ),
        serialization_alias='https://schema.org/drug'
    )
