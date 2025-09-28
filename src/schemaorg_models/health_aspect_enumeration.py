from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HealthAspectEnumeration(Enumeration):
    """
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].
    """
    class_: Literal['https://schema.org/HealthAspectEnumeration'] = Field( # type: ignore
        default='https://schema.org/HealthAspectEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
