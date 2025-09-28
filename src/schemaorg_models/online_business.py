from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.organization import Organization

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OnlineBusiness(Organization):
    """
A particular online business, either standalone or the online part of a broader organization. Examples include an eCommerce site, an online travel booking site, an online learning site, an online logistics and shipping provider, an online (virtual) doctor, etc.
    """
    class_: Literal['https://schema.org/OnlineBusiness'] = Field( # type: ignore
        default='https://schema.org/OnlineBusiness',
        alias='@type',
        serialization_alias='@type'
    )
