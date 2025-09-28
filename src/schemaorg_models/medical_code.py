from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_intangible import MedicalIntangible

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class MedicalCode(MedicalIntangible):
    """
A code for a medical entity.
    """
    class_: Literal['https://schema.org/MedicalCode'] = Field( # type: ignore
        default='https://schema.org/MedicalCode',
        alias='@type',
        serialization_alias='@type'
    )
    codingSystem: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codingSystem',
            'https://schema.org/codingSystem'
        ),
        serialization_alias='https://schema.org/codingSystem'
    )
    codeValue: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codeValue',
            'https://schema.org/codeValue'
        ),
        serialization_alias='https://schema.org/codeValue'
    )
