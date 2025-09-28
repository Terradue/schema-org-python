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

class DryCleaningOrLaundry(LocalBusiness):
    """
A dry-cleaning business.
    """
    class_: Literal['https://schema.org/DryCleaningOrLaundry'] = Field( # type: ignore
        default='https://schema.org/DryCleaningOrLaundry',
        alias='@type',
        serialization_alias='@type'
    )
