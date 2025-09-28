from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

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

class WebSite(CreativeWork):
    """
A WebSite is a set of related web pages and other items typically served from a single web domain and accessible via URLs.
    """
    class_: Literal['https://schema.org/WebSite'] = Field( # type: ignore
        default='https://schema.org/WebSite',
        alias='@type',
        serialization_alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issn',
            'https://schema.org/issn'
        ),
        serialization_alias='https://schema.org/issn'
    )
