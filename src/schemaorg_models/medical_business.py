from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.local_business import LocalBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalBusiness(LocalBusiness):
    """
A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals.
    """
    class_: Literal['https://schema.org/MedicalBusiness'] = Field( # type: ignore
        default='https://schema.org/MedicalBusiness',
        alias='@type',
        serialization_alias='@type'
    )
