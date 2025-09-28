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

class MedicalTestPanel(MedicalTest):
    """
Any collection of tests commonly ordered together.
    """
    class_: Literal['https://schema.org/MedicalTestPanel'] = Field( # type: ignore
        default='https://schema.org/MedicalTestPanel',
        alias='@type',
        serialization_alias='@type'
    )
    subTest: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subTest',
            'https://schema.org/subTest'
        ),
        serialization_alias='https://schema.org/subTest'
    )
