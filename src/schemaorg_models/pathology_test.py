from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_test import MedicalTest

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

class PathologyTest(MedicalTest):
    """
A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.
    """
    class_: Literal['https://schema.org/PathologyTest'] = Field( # type: ignore
        default='https://schema.org/PathologyTest',
        alias='@type',
        serialization_alias='@type'
    )
    tissueSample: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tissueSample',
            'https://schema.org/tissueSample'
        ),
        serialization_alias='https://schema.org/tissueSample'
    )
