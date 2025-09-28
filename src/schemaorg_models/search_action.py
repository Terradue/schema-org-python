from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.action import Action

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

class SearchAction(Action):
    """
The act of searching for an object.\
\
Related actions:\
\
* [[FindAction]]: SearchAction generally leads to a FindAction, but not necessarily.
    """
    class_: Literal['https://schema.org/SearchAction'] = Field( # type: ignore
        default='https://schema.org/SearchAction',
        alias='@type',
        serialization_alias='@type'
    )
    query: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'query',
            'https://schema.org/query'
        ),
        serialization_alias='https://schema.org/query'
    )
