from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.role import Role

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
from schemaorg_models.language import Language

class LinkRole(Role):
    """
A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.
    """
    class_: Literal['https://schema.org/LinkRole'] = Field( # type: ignore
        default='https://schema.org/LinkRole',
        alias='@type',
        serialization_alias='@type'
    )
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
    linkRelationship: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'linkRelationship',
            'https://schema.org/linkRelationship'
        ),
        serialization_alias='https://schema.org/linkRelationship'
    )
