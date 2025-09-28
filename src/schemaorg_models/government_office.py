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

class GovernmentOffice(LocalBusiness):
    """
A government office&#x2014;for example, an IRS or DMV office.
    """
    class_: Literal['https://schema.org/GovernmentOffice'] = Field( # type: ignore
        default='https://schema.org/GovernmentOffice',
        alias='@type',
        serialization_alias='@type'
    )
