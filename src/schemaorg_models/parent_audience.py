from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.people_audience import PeopleAudience

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

class ParentAudience(PeopleAudience):
    """
A set of characteristics describing parents, who can be interested in viewing some content.
    """
    class_: Literal['https://schema.org/ParentAudience'] = Field( # type: ignore
        default='https://schema.org/ParentAudience',
        alias='@type',
        serialization_alias='@type'
    )
    childMaxAge: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'childMaxAge',
            'https://schema.org/childMaxAge'
        ),
        serialization_alias='https://schema.org/childMaxAge'
    )
    childMinAge: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'childMinAge',
            'https://schema.org/childMinAge'
        ),
        serialization_alias='https://schema.org/childMinAge'
    )
