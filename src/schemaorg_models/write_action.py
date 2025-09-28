from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.create_action import CreateAction

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

class WriteAction(CreateAction):
    """
The act of authoring written creative content.
    """
    class_: Literal['https://schema.org/WriteAction'] = Field( # type: ignore
        default='https://schema.org/WriteAction',
        alias='@type',
        serialization_alias='@type'
    )
    language: Optional[Union[Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'language',
            'https://schema.org/language'
        ),
        serialization_alias='https://schema.org/language'
    )
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inLanguage',
            'https://schema.org/inLanguage'
        ),
        serialization_alias='https://schema.org/inLanguage'
    )
