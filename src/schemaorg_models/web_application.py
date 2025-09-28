from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.software_application import SoftwareApplication

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

class WebApplication(SoftwareApplication):
    """
Web applications.
    """
    class_: Literal['https://schema.org/WebApplication'] = Field( # type: ignore
        default='https://schema.org/WebApplication',
        alias='@type',
        serialization_alias='@type'
    )
    browserRequirements: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'browserRequirements',
            'https://schema.org/browserRequirements'
        ),
        serialization_alias='https://schema.org/browserRequirements'
    )
